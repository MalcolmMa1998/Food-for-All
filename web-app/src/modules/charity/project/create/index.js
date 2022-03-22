/**
 * @file Project creating page
 * @author Mingze Ma
 */

import {useDispatch, useSelector} from 'react-redux';
import React, {useEffect} from 'react';
import {
  Form,
  Input,
  InputNumber,
  Select,
  Button,
  DatePicker, Upload,
} from 'antd';
import actions from 'src/actions';
import {InboxOutlined} from "@ant-design/icons";
import moment from "moment";

const {RangePicker} = DatePicker;
const {Option} = Select;

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};

const validateMessages = {
  required: '${label} is required!',
  types: {
    email: '${label} is not a valid email!',
    number: '${label} is not a valid number!',
  },
  number: {
    range: '${label} must be between ${min} and ${max}',
  },
};

const handleUpload = async (file) => {
  console.log('--file--\n', file);
};

const normFile = (e) => {
  console.log('Upload event:', e);

  if (Array.isArray(e)) {
    return e;
  }

  return e && e.fileList;
};

const rangeConfig = {
  rules: [{type: 'array', required: false, message: 'Please select time!'}],
};

export default () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(actions.getUserInfo());
    dispatch(actions.getCurrencyList());
  }, [dispatch]);

  const {userInfo} = useSelector(state => state.user);
  const {currencyList} = useSelector(state => state.global);

  const suffixSelector = (
    <Form.Item name="currency" noStyle>
      <Select
        showSearch
        style={{width: 200}}
        placeholder="Search to Select"
        optionFilterProp="children"
        filterOption={(input, option) =>
          option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
        }
        filterSort={(optionA, optionB) =>
          optionA.children.toLowerCase().localeCompare(optionB.children.toLowerCase())
        }
      >
        {currencyList.map(item => (
          <Option value={item} key={item}>{item}</Option>
        ))}
      </Select>
    </Form.Item>
  );

  const logout = () => {
    actions.logout();
    console.log('logout');
  }

  const onFinish = async (values) => {
    try {
      const createProjectRes = await actions.createProject();
      console.log('createProjectRes.status\n', createProjectRes);
      if (createProjectRes.status === 0) {
        const editProjectRes = await actions.editProject({
          "pid": createProjectRes.pid,
          "currency_type": values.currency,
          "edit": {
            "title": values.title,
            "intro": values.introduction,
            "background_image": "",
            "total_num": values.donation,
            "start_time": moment(values.projectTime[0]).valueOf(),
            "end_time": moment(values.projectTime[1]).valueOf(),
            "details": values.details,
            "price": 100
          }
        });
      }
    } catch (e) {

    }
  };

  return (
    <Form {...layout}
          name="nest-messages"
          onFinish={onFinish}
          validateMessages={validateMessages}
          initialValues={{
            currency: userInfo.currency_type
          }}
    >

      <Form.Item name="title" label="Title" rules={[{required: false, message: 'Please input the title'}]}>
        <Input/>
      </Form.Item>

      <Form.Item
        // name="donation"
        name="donation"
        label="Donation Amount"
        rules={[{required: false, message: 'Please input donation amount!'}]}
      >
        <InputNumber addonAfter={suffixSelector} style={{width: '100%'}}/>
      </Form.Item>

      <Form.Item name="projectTime" label="RangePicker" {...rangeConfig}>
        <RangePicker/>
      </Form.Item>

      <Form.Item name="introduction" label="Introduction">
        <Input.TextArea/>
      </Form.Item>

      <Form.Item name="details" label="Details">
        <Input.TextArea/>
      </Form.Item>

      <Form.Item label="Backgrund Image">
        <Form.Item name="background_image" valuePropName="fileList" getValueFromEvent={normFile} noStyle>
          <Upload.Dragger name="files" action={handleUpload}>
            <p className="ant-upload-drag-icon">
              <InboxOutlined/>
            </p>
            <p className="ant-upload-text">Click or drag file to this area to upload</p>
            <p className="ant-upload-hint">Support for a single or bulk upload.</p>
          </Upload.Dragger>
        </Form.Item>
      </Form.Item>

      <Form.Item wrapperCol={{...layout.wrapperCol, offset: 8}}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>

      <Form.Item wrapperCol={{...layout.wrapperCol, offset: 8}}>
        <Button type="primary" onClick={logout}>
          Logout
        </Button>
      </Form.Item>
    </Form>
  );
};

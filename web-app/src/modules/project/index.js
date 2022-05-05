/**
 * @file project list for donors and guests
 * @author Mingze Ma
 */

import { forwardRef, useCallback, useEffect, useState } from 'react';
// material
import { Container, Stack, Typography } from '@mui/material';
// components
import { ProjectList } from 'src/components/ProjectCardList';
//
import _ from "lodash";
// material
import { Box } from '@mui/material';

import actions from "src/actions";
import { useDispatch, useSelector } from "react-redux";
import { DEFAULT_CURRENCY } from "src/constants/constants";
// ----------------------------------------------------------------------

export default (props) => {

  const {} = props;
  const dispatch = useDispatch();
  const [projectInfo, setProjectInfo] = useState({});
  const [prepareMode, setPrepareMode] = useState(false);
  const { userInfo } = useSelector(state => state.user);

  const getProjectList = useCallback(async () => {
    try {
      let res = {};
      if (prepareMode) {
        res = await actions.getPrepareProject();
      } else {
        res = await actions.getProjectList({
          currency_type: userInfo.currency_type || DEFAULT_CURRENCY,
          page_info: {
            page_size: 10000,
            page: 1
          },
          search: '',
          order: 'charity',
          uid: '',
          valid_only: '',
        });
      }
      const {
        project_info: rawProjectInfo,
        page_info: pageInfo,
        currency_type: currencyType,
        ...otherProps
      } = res;
      const projectInfo = _.values(rawProjectInfo);
      const result = {
        ...otherProps,
        projectInfo,
        pageInfo,
        currencyType,
      };
      setProjectInfo(result);//设置projectInfo需要使用这个
    } catch (e) {
      console.error(e);
    }
  }, [prepareMode, userInfo.currency_type]);

  useEffect(() => {
    getProjectList().catch(err => console.error(err));
    dispatch(actions.getRegionList());
  }, [dispatch, getProjectList]);

  return (
    <div className="project">
      <Box>
        <h1>ProjectList</h1>
        <Box>
          <Container>
            <ProjectList projects={_.get(projectInfo, 'projectInfo', [])} />
          </Container>
        </Box>
      </Box>
    </div>
  );
}

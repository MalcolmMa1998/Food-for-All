/**
 * @file route config
 * @author Mingze Ma
 */

import loadable from 'react-loadable';
import { Spin } from "antd";

const Loading = () => <Spin size="large"/>

export default [
  {
    path: '/',
    component: loadable({
      loader: () => import(/* webpackChunkName: 'login' */ /* webpackMode: 'lazy' */ 'src/modules/home'),
      loading: Loading,
    }),
    exact: true,
  },
  {
    path: '/login',
    component: loadable({
      loader: () => import(/* webpackChunkName: 'login' */ /* webpackMode: 'lazy' */ 'src/modules/login'),
      loading: Loading,
    }),
    exact: true,
  },
];

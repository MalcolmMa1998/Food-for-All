/**
 * @file action entry
 * @author Mingze Ma
 */

import * as userActions from './userActions';
import * as projectActions from './projectActions';


export default {
  ...userActions,
  ...projectActions,
};

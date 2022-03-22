/**
 * @file login page index
 * @author Mingze Ma
 */

import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from 'react-router-dom';
import _ from 'lodash';
import Alert from '@mui/material/Alert';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useCallback, useEffect, useState } from "react";
import { message } from 'antd';

import actions from "src/actions";
import { LOGIN_STATUS } from 'src/constants/constants';

const theme = createTheme();

export default (props) => {
  const {} = props;

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const userInfo = useSelector(state => state.user.userInfo);

  const [showError, setShowError] = useState(false);
  const [preCheck, setPreCheck] = useState(_.get(userInfo, 'isLoggedIn', false));

  const handleSubmit = useCallback(async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });
    try {
      // call login api
      const res = await dispatch(actions.login({
        username: data.get('email'),
        password: data.get('password'),
      }));
      // login error
      if (res.status && res.status !== LOGIN_STATUS['success']) {
        setShowError(true);
        setTimeout(() => setShowError(false), 3000);
        return;
      }
      if (_.get(res, 'uid', null)) {
        navigate('/', );
        message.success('Login successfully!');
      }
    } catch (e) {
      console.error(e);
    }
  }, [dispatch, navigate]);

  useEffect(() => {
    console.log(_.get(userInfo, 'isLoggedIn'));
    if (preCheck) {
      navigate('/');
      message.warning('You have already logged in!');
    }
  }, [navigate, preCheck]);

  return (
    <div className="ffa-login">
      {
        !preCheck && <ThemeProvider theme={theme}>
          {showError && <Alert severity="error" onClose={() => setShowError(false)}>
            Invalid Username or Password, please try again.
          </Alert>}
          <Container component="main" maxWidth="xs">
            <CssBaseline/>
            <Box
              sx={{
                marginTop: 8,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
              }}
            >
              <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                <LockOutlinedIcon/>
              </Avatar>
              <Typography component="h1" variant="h5">
                Sign in
              </Typography>
              <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                <TextField
                  margin="normal"
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                  autoFocus
                />
                <TextField
                  margin="normal"
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="current-password"
                />
                <FormControlLabel
                  control={<Checkbox value="remember" color="primary"/>}
                  label="Remember me"
                />
                <Button
                  type="submit"
                  fullWidth
                  variant="contained"
                  sx={{ mt: 3, mb: 2 }}
                >
                  Sign In
                </Button>
                <Grid container>
                  <Grid item xs>
                    <Link href="#" variant="body2">
                      Forgot password?
                    </Link>
                  </Grid>
                  <Grid item>
                    <Link onClick={() => navigate('/register')} variant="body2">
                      {"Don't have an account? Sign Up"}
                    </Link>
                  </Grid>
                </Grid>
              </Box>
            </Box>
          </Container>
        </ThemeProvider>
      }
    </div>
  );
};

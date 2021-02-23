import React from 'react';
import { Form, Input, Button, Checkbox, InputNumber } from 'antd';
import './App.css';

const App = () => {
  const onFinish = (values) => {
    console.log('Success:', values);
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (
   <div><h1> Availity Sign-Up! </h1>
   <div style={{width: 450, marginTop: 75}}>
    <Form
      name="basic"
      initialValues={{
        remember: true,
      }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        label="First Name"
        name="fname"
        rules={[
          {
            required: true,
            message: 'Please input your First Name!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Last Name"
        name="lname"
        rules={[
          {
            required: true,
            message: 'Please input your Last Name!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="NPI Number"
        name="npiNumber"
        rules={[
          {
            required: true,
            message: 'Please input your NPI Number!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Business Address"
        name="bizAddr"
        rules={[
          {
            required: true,
            message: 'Please input your Business Address!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Telephone Number"
        name="tele"
        rules={[
          {
            required: true,
            message: 'Please input your Telephone Number!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="First Name"
        name="fname"
        rules={[
          {
            required: true,
            message: 'Please input your First Name!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Email"
        name="email"
        rules={[
                { type: 'email', message: 'Please use a valid email' },
                { required: true, message: 'We need your email to create your account' }
               ]}
                >
                <Input
                  placeholder="Enter your email"
                  maxLength={64} />
      </Form.Item>


      <Form.Item
        label="Password"
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your password!',
          },
        ]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
    </div>
    </div>
  );
};

export default App
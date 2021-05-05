<template>
  <div id="login_container">
    <div id="login_box">
      <p id="login_title">船舶机务管理系统</p>
      <el-form id="login_form" :model="loginForm" :rules="login_rules" ref="loginFormRef">
        <el-form-item prop="username">
          <el-input v-model="loginForm.username" placeholder="账号" prefix-icon="el-icon-user"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="loginForm.password" placeholder="密码" prefix-icon="el-icon-lock" type="password"></el-input>
        </el-form-item>
        <el-form-item id="button">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button type="info" @click="resetLoginForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      loginForm: {
        username: 'admin',
        password: 'admin'
      },
      login_rules: {
        username: [
          { required: true, message: '请输入账号', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    resetLoginForm () {
      this.$refs.loginFormRef.resetFields()
    },
    login () {
      this.$refs.loginFormRef.validate(async valid => {
        if (!valid) return false
        const result = await this.$axios.post('login/', this.loginForm)
        if (result.status === 200) {
          this.$message.success('登录成功')
          console.log(result)
          window.sessionStorage.setItem('token', result.data.token)
          this.$router.push('/home')
        } else {
          return this.$message.error('登录成功')
        }
      })
    }
  }
}
</script>

<style scoped>
#login_container {
  background-color: #6699CC;
  height: 100%;
}

#login_box {
  position:absolute;
  top: 50%;
  left: 50%;
  width: 28rem;
  height: 21rem;
  background-color: white;
  border-radius: 1rem;
  transform: translate(-50%,-50%);
}

#button {
  display: flex;
  justify-content:flex-end;
}

#login_form {
  position:absolute;
  bottom: 0;
  width: 100%;
  padding: 0 2rem;
  box-sizing: border-box;
}

#login_title {
  text-align: center;
  color: #003366;
  font-size: 1.5em;
  font-family: "PingFang SC";
}
</style>

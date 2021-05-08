<template>
  <el-container class="page">
    <!--头部区域-->
    <el-header>
      <div>
        <p class="page_title">船舶机务管理系统</p>
      </div>
      <el-button type="danger" @click="logout">退出登录</el-button>
    </el-header>
    <!--主体区域-->
    <el-container>
      <!--侧边栏-->
      <el-aside width="200px">
        <el-menu class="aside_meun" router>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-connection"></i>
              <span>基本信息管理</span>
            </template>
            <el-menu-item index="personnel">人员管理</el-menu-item>
            <el-menu-item index="department">部门管理</el-menu-item>
            <el-menu-item index="ship">船盘信息管理</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!--主体-->
      <el-main><router-view></router-view></el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  methods: {
    logout() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.page_title {
  font-size: 1.3em;
}

.el-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.aside_meun {
  height: 100%;
}
</style>

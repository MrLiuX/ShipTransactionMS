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
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-connection"></i>
              <span>基本信息管理</span>
            </template>
            <el-menu-item index="personnel">人员管理</el-menu-item>
            <el-menu-item index="department">部门管理</el-menu-item>
            <el-menu-item index="ship">船盘信息管理</el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-box"></i>
              <span>物料管理</span>
            </template>
            <el-menu-item index="inventory">库存管理</el-menu-item>
            <el-menu-item index="storage">入库申请</el-menu-item>
            <el-menu-item index="approval">申请审批</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-bank-card"></i>
              <span>费用管理</span>
            </template>
          </el-submenu>
          <el-submenu index="4">
            <template slot="title">
              <i class="el-icon-document"></i>
              <span>船舶证书管理</span>
            </template>
            <el-menu-item index="certificate">库存管理</el-menu-item>
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
  created() {
    this.open2()
  },
  methods: {
    logout() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    open2() {
      this.$notify({
        title: '提示',
        message: '您有一条待审批的申请',
        duration: 0
      })
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

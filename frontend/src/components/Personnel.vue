<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <el-breadcrumb separator="/" class="bread-head">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>基本信息管理</el-breadcrumb-item>
          <el-breadcrumb-item>人员管理</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="username" label="员工编号" width="100px">
        </el-table-column>
        <el-table-column prop="name" label="姓名" width="100px">
        </el-table-column>
        <el-table-column prop="mobileNumber" label="手机号码">
        </el-table-column>
        <el-table-column prop="teleNumber" label="固定电话"> </el-table-column>
        <el-table-column prop="department" label="部门" width="80px">
        </el-table-column>
        <el-table-column prop="address" label="家庭住址" width="400px">
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: []
    }
  },
  created() {
    this.getpersonnelList()
  },
  methods: {
    async getpersonnelList() {
      const { data: res } = await this.$axios.get('/api/personnel/')
      this.tableData = res
    }
  }
}
</script>

<style scoped>
.bread-head {
  padding: 1rem;
}
</style>

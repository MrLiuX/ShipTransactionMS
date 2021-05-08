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
      <div>
        <div>
          <el-input
            placeholder="请输入员工编号进行搜索"
            class="search-input"
            v-model="searchId"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getPersonnel"
            ></el-button>
          </el-input>
          <el-button @click="dialogFormVisible = true">添加员工</el-button>
        </div>
        <div>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="username" label="员工编号" width="150px">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="100px">
            </el-table-column>
            <el-table-column prop="mobileNumber" label="手机号码">
            </el-table-column>
            <el-table-column prop="teleNumber" label="固定电话">
            </el-table-column>
            <el-table-column prop="department" label="部门" width="80px">
            </el-table-column>
            <el-table-column prop="address" label="家庭住址" width="400px">
            </el-table-column>
          </el-table>
        </div>
      </div>
    </el-card>
    <el-dialog title="添加员工" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="员工编号" :label-width="formLabelWidth">
          <el-input v-model="form.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="员工初始密码" :label-width="formLabelWidth">
          <el-input v-model="form.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="手机号码" :label-width="formLabelWidth">
          <el-input v-model="form.mobileNumber" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="固定电话" :label-width="formLabelWidth">
          <el-input v-model="form.teleNumber" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="家庭住址" :label-width="formLabelWidth">
          <el-input v-model="form.address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="部门" :label-width="formLabelWidth">
          <el-select v-model="form.department" placeholder="请选择所处部门">
            <el-option
              :label="dData.department"
              :value="dData.department"
              v-for="dData in departmentData"
              :key="dData.department"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="addPersonnel">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="搜索结果"
      :visible.sync="dialogTableVisible"
      @closed="dialogClose"
    >
      <el-table :data="tableData1">
        <el-table-column prop="username" label="员工编号" width="80px">
        </el-table-column>
        <el-table-column prop="name" label="姓名" width="60px">
        </el-table-column>
        <el-table-column prop="mobileNumber" label="手机号码">
        </el-table-column>
        <el-table-column prop="teleNumber" label="固定电话"> </el-table-column>
        <el-table-column prop="department" label="部门" width="80px">
        </el-table-column>
        <el-table-column prop="address" label="家庭住址" width="200px">
        </el-table-column>
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="danger" plain @click="deletePersonnel"
          >删除员工</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [],
      tableData1: [],
      departmentData: [],
      dialogFormVisible: false,
      dialogTableVisible: false,
      searchInfo: '',
      searchId: '',
      form: {
        username: '',
        password: '',
        name: '',
        mobileNumber: '',
        teleNumber: '',
        department: '',
        address: ''
      },
      formLabelWidth: '100px'
    }
  },
  created() {
    this.getpersonnelList()
    this.getDepartmentList()
  },
  methods: {
    async getpersonnelList() {
      const { data: res } = await this.$axios.get('/api/personnels/')
      this.tableData = res
    },
    async getDepartmentList() {
      const { data: res2 } = await this.$axios.get('/api/departments/')
      this.departmentData = res2
    },
    async addPersonnel() {
      const res3 = await this.$axios.post('/api/personnels/', this.form)
      if (res3.data.name) {
        this.$message.success('添加成功')
      }
      this.dialogFormVisible = false
      window.location.reload()
    },
    async getPersonnel() {
      const { data: res4 } = await this.$axios.get(
        '/api/personnels/' + this.searchId
      )
      this.tableData1.push(res4)
      this.dialogTableVisible = true
      console.log(this.searchInfo)
    },
    dialogClose() {
      this.tableData1 = []
    },
    deletePersonnel() {
      this.$axios.delete('/api/personnels/' + this.tableData1[0].username + '/')
      this.$message.success('删除成功')
      this.dialogTableVisible = false
      window.location.reload()
    }
  }
}
</script>

<style scoped>
.search-input {
  width: 20rem;
  padding: 1rem;
}
</style>

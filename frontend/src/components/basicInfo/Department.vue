<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <el-breadcrumb separator="/" class="bread-head">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>基本信息管理</el-breadcrumb-item>
          <el-breadcrumb-item>部门管理</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
      <div>
        <div>
          <el-input
            placeholder="请输入部门名称进行搜索"
            class="search-input"
            v-model="searchId"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getDepartment"
            ></el-button>
          </el-input>
          <el-button @click="addDepartmentDialogVisible = true"
            >添加部门</el-button
          >
        </div>
        <div>
          <el-table :data="deparmtnetListData" style="width: 100%">
            <el-table-column prop="department" label="部门"> </el-table-column>
            <el-table-column prop="minister" label="部门管理员">
            </el-table-column>
            <el-table-column prop="note" label="备注"> </el-table-column>
          </el-table>
        </div>
      </div>
    </el-card>

    <el-dialog title="添加部门" :visible.sync="addDepartmentDialogVisible">
      <el-form :model="addDepartmentForm">
        <el-form-item label="部门名称" :label-width="formLabelWidth">
          <el-input
            v-model="addDepartmentForm.department"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="部门管理员" :label-width="formLabelWidth">
          <el-input
            v-model="addDepartmentForm.minister"
            autocomplete="off"
            placeholder="若为空请填写无"
          ></el-input>
        </el-form-item>
        <el-form-item label="备注" :label-width="formLabelWidth">
          <el-input
            v-model="addDepartmentForm.note"
            autocomplete="off"
            placeholder="若为空请填写无"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addDepartmentDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addDepartment">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="搜索结果"
      :visible.sync="searchDepartmentDialogVisible"
      @closed="dialogClose"
    >
      <el-table :data="searchResult">
        <el-table-column prop="department" label="部门名称"> </el-table-column>
        <el-table-column prop="minister" label="部门管理员"> </el-table-column>
        <el-table-column prop="note" label="备注"> </el-table-column>
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="danger" plain @click="deleteDepartment"
          >删除部门</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchId: '',
      searchResult: [],
      addDepartmentDialogVisible: false,
      searchDepartmentDialogVisible: false,
      deparmtnetListData: [],
      formLabelWidth: '100px',
      addDepartmentForm: {
        department: '',
        minister: '',
        note: ''
      }
    }
  },
  created() {
    this.getDepartmentList()
  },
  methods: {
    async getDepartmentList() {
      const { data: result } = await this.$axios.get('/api/departments/')
      this.deparmtnetListData = result
    },
    async getDepartment() {
      const { data: result } = await this.$axios.get(
        '/api/departments/' + this.searchId + '/'
      )
      this.searchResult.push(result)
      this.searchDepartmentDialogVisible = true
    },
    async addDepartment() {
      const result = await this.$axios.post(
        '/api/departments/',
        this.addDepartmentForm
      )
      if (result.data.department) {
        this.$message.success('添加成功')
      }
      this.addDepartmentDialogVisible = false
      window.location.reload()
    },
    deleteDepartment() {
      this.$axios.delete(
        '/api/departments/' + this.searchResult[0].department + '/'
      )
      this.$message.success('删除成功')
      this.dialogTableVisible = false
      window.location.reload()
    },
    dialogClose() {
      this.searchResult = []
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

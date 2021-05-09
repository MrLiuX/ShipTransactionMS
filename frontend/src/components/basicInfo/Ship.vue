<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <el-breadcrumb separator="/" class="bread-head">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>基本信息管理</el-breadcrumb-item>
          <el-breadcrumb-item>船盘信息管理</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
      <div>
        <div>
          <el-input
            placeholder="请输入船盘名称进行搜索"
            class="search-input"
            v-model="searchId"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getShip"
            ></el-button>
          </el-input>
          <el-button @click="addShipDialogVisible = true"
            >添加船盘信息</el-button
          >
        </div>
        <div>
          <el-table :data="shipListData" style="width: 100%">
            <el-table-column prop="name" label="船名"> </el-table-column>
            <el-table-column prop="manufactureTime" label="制造时间">
            </el-table-column>
            <el-table-column prop="manufactureDress" label="制造地点">
            </el-table-column>
            <el-table-column prop="flag" label="船旗"> </el-table-column>
            <el-table-column prop="level" label="船级"> </el-table-column>
            <el-table-column prop="port" label="船籍港"> </el-table-column>
            <el-table-column prop="tonnageTotal" label="总吨">
            </el-table-column>
            <el-table-column prop="tonnageNet" label="净吨"> </el-table-column>
            <el-table-column prop="size" label="船舶尺寸"> </el-table-column>
            <el-table-column prop="power" label="主机及功率"> </el-table-column>
            <el-table-column prop="location" label="存放位置">
            </el-table-column>
          </el-table>
        </div>
      </div>
    </el-card>

    <el-dialog title="添加船盘信息" :visible.sync="addShipDialogVisible">
      <el-form :model="addShipForm">
        <el-form-item label="船名" :label-width="formLabelWidth">
          <el-input v-model="addShipForm.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="制造时间" :label-width="formLabelWidth">
          <el-input
            v-model="addShipForm.manufactureTime"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="制造地点" :label-width="formLabelWidth">
          <el-input
            v-model="addShipForm.manufactureDress"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="船旗" :label-width="formLabelWidth">
          <el-input v-model="addShipForm.flag" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="船级" :label-width="formLabelWidth">
          <el-input v-model="addShipForm.level" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="船籍港" :label-width="formLabelWidth">
          <el-input v-model="addShipForm.port" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="总吨" :label-width="formLabelWidth">
          <el-input
            v-model="addShipForm.tonnageTotal"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="净吨" :label-width="formLabelWidth">
          <el-input
            v-model="addShipForm.tonnageNet"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="船舶尺寸" :label-width="formLabelWidth">
          <el-input v-model="addShipForm.size" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="主机及功率" :label-width="formLabelWidth">
          <el-input v-model="addShipForm.power" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="存放位置" :label-width="formLabelWidth">
          <el-input
            v-model="addShipForm.location"
            autocomplete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addShipDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addShip">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="搜索结果"
      :visible.sync="searchShipDialogVisible"
      @closed="dialogClose"
    >
      <el-table :data="searchResult">
        <el-table-column prop="name" label="船名"> </el-table-column>
        <el-table-column prop="manufactureTime" label="制造时间">
        </el-table-column>
        <el-table-column prop="manufactureDress" label="制造地点">
        </el-table-column>
        <el-table-column prop="flag" label="船旗"> </el-table-column>
        <el-table-column prop="level" label="船级"> </el-table-column>
        <el-table-column prop="port" label="船籍港"> </el-table-column>
        <el-table-column prop="tonnageTotal" label="总吨"> </el-table-column>
        <el-table-column prop="tonnageNet" label="净吨"> </el-table-column>
        <el-table-column prop="size" label="船舶尺寸"> </el-table-column>
        <el-table-column prop="power" label="主机及功率"> </el-table-column>
        <el-table-column prop="location" label="存放位置"> </el-table-column>
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="danger" plain @click="deleteShip"
          >删除船盘信息</el-button
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
      addShipDialogVisible: false,
      searchShipDialogVisible: false,
      shipListData: [],
      formLabelWidth: '100px',
      addShipForm: {
        name: '',
        manufactureTime: '',
        manufactureDress: '',
        flag: '',
        level: '',
        port: '',
        tonnageTotal: '',
        tonnageNet: '',
        size: '',
        power: '',
        location: ''
      }
    }
  },
  created() {
    this.getShipList()
  },
  methods: {
    async getShipList() {
      const { data: result } = await this.$axios.get('/api/ships/')
      this.shipListData = result
    },
    async getShip() {
      const { data: result } = await this.$axios.get(
        '/api/ships/' + this.searchId + '/'
      )
      this.searchResult.push(result)
      this.searchShipDialogVisible = true
    },
    async addShip() {
      const result = await this.$axios.post('/api/ships/', this.addShipForm)
      if (result.data.Ship) {
        this.$message.success('添加成功')
      }
      this.addShipDialogVisible = false
      window.location.reload()
    },
    deleteShip() {
      this.$axios.delete('/api/ships/' + this.searchResult[0].name + '/')
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

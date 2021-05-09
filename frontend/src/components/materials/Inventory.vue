<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <el-breadcrumb separator="/" class="bread-head">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>物料管理</el-breadcrumb-item>
          <el-breadcrumb-item>库存管理</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
      <div>
        <div>
          <el-input
            placeholder="请输入物料名称进行搜索"
            class="search-input"
            v-model="searchId"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getInventory"
            ></el-button>
          </el-input>
          <el-button @click="addInventoryDialogVisible = true"
            >添加物料信息</el-button
          >
        </div>
        <div>
          <el-table :data="inventoryListData" style="width: 100%">
            <el-table-column type="expand">
              <template slot-scope="props">
                <el-form label-position="left" inline class="demo-table-expand">
                  <el-form-item label="物料">
                    <span>{{ props.row.name }}</span>
                  </el-form-item>
                  <el-form-item label="所属船只">
                    <span>{{ props.row.ship }}</span>
                  </el-form-item>
                  <el-form-item label="分类">
                    <span>{{ props.row.category }}</span>
                  </el-form-item>
                  <el-form-item label="存放位置">
                    <span>{{ props.row.location }}</span>
                  </el-form-item>
                  <el-form-item label="累计入库">
                    <span>{{ props.row.accumulativeStorage }}</span>
                  </el-form-item>
                  <el-form-item label="累计出库">
                    <span>{{ props.row.accumulativeUnStorage }}</span>
                  </el-form-item>
                  <el-form-item label="备注">
                    <span>{{ props.row.note }}</span>
                  </el-form-item>
                </el-form>
              </template>
            </el-table-column>
            <el-table-column prop="name" label="物料"> </el-table-column>
            <el-table-column prop="specification" label="规格">
            </el-table-column>
            <el-table-column prop="inventory" label="现库存量">
            </el-table-column>
            <el-table-column prop="inventoryUpperLimit" label="库存上限">
            </el-table-column>
            <el-table-column prop="inventoryLowerLimit" label="库存下限">
            </el-table-column>
            <el-table-column prop="unit" label="单位"> </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="primary"
                  plain
                  @click="handleEdit(scope.$index, scope.row)"
                  >申请采购入库</el-button
                >
                <el-button
                  size="mini"
                  type="success"
                  plain
                  @click="handleDelete(scope.$index, scope.row)"
                  >申请出库</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>
    </el-card>

    <el-dialog title="添加物料信息" :visible.sync="addInventoryDialogVisible">
      <el-form :model="addInventoryForm">
        <el-form-item label="物料名称" :label-width="formLabelWidth">
          <el-input
            v-model="addInventoryForm.name"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="规格" :label-width="formLabelWidth">
          <el-input
            v-model="addInventoryForm.specification"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="分类" :label-width="formLabelWidth">
          <el-input
            v-model="addInventoryForm.category"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="计数单位" :label-width="formLabelWidth">
          <el-input
            v-model="addInventoryForm.unit"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="库存上限" :label-width="formLabelWidth">
          <el-input
            v-model="addInventoryForm.inventoryUpperLimit"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="库存下限" :label-width="formLabelWidth">
          <el-input
            v-model="addInventoryForm.inventoryLowerLimit"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="存放位置" :label-width="formLabelWidth">
          <el-input
            v-model="addInventoryForm.location"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="备注" :label-width="formLabelWidth">
          <el-input
            v-model="addInventoryForm.note"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="所属船只" :label-width="formLabelWidth">
          <el-select
            v-model="addInventoryForm.ship"
            placeholder="请选择所属船只"
          >
            <el-option
              :label="dData.name"
              :value="dData.name"
              v-for="dData in ShipListData"
              :key="dData.name"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addInventoryDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addInventory">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="搜索结果"
      :visible.sync="searchInventoryDialogVisible"
      @closed="dialogClose"
    >
      <el-table :data="searchResult">
        <el-table-column prop="name" label="物料"> </el-table-column>
        <el-table-column prop="specification" label="规格"> </el-table-column>
        <el-table-column prop="inventory" label="现库存量"> </el-table-column>
        <el-table-column prop="inventoryUpperLimit" label="库存上限">
        </el-table-column>
        <el-table-column prop="inventoryLowerLimit" label="库存下限">
        </el-table-column>
        <el-table-column prop="unit" label="单位"> </el-table-column>
        <el-table-column prop="accumulativeStorage" label="累计入库">
        </el-table-column>
        <el-table-column prop="accumulativeUnStorage" label="累计出库">
        </el-table-column>
        <el-table-column prop="ship" label="所属船只"> </el-table-column>
        <el-table-column prop="category" label="分类"> </el-table-column>
        <el-table-column prop="location" label="存放位置"> </el-table-column>
        <el-table-column prop="note" label="备注"> </el-table-column>
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="danger" plain @click="deleteInventory"
          >删除物料</el-button
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
      searchInventoryDialogVisible: false,
      addInventoryDialogVisible: false,
      inventoryListData: [],
      ShipListData: [],
      formLabelWidth: '100px',
      addInventoryForm: {
        ship: '',
        category: '',
        name: '',
        specification: '',
        unit: '',
        location: '',
        accumulativeStorage: '0',
        accumulativeUnStorage: '0',
        inventory: '0',
        inventoryUpperLimit: '',
        inventoryLowerLimit: '',
        note: ''
      }
    }
  },
  created() {
    this.getInventoryList()
    this.getShipList()
  },
  methods: {
    async getShipList() {
      const { data: result } = await this.$axios.get('/api/ships/')
      this.ShipListData = result
      console.log(this.ShipListData)
    },
    async getInventoryList() {
      const { data: result } = await this.$axios.get('/api/inventorys/')
      this.inventoryListData = result
    },
    async getInventory() {
      const { data: result } = await this.$axios.get(
        '/api/inventorys/' + this.searchId + '/'
      )
      this.searchResult.push(result)
      this.searchInventoryDialogVisible = true
    },
    async addInventory() {
      const result = await this.$axios.post(
        '/api/inventorys/',
        this.addInventoryForm
      )
      if (result.data.inventory) {
        this.$message.success('添加成功')
      }
      this.addInventoryDialogVisible = false
      window.location.reload()
    },
    deleteInventory() {
      this.$axios.delete('/api/inventorys/' + this.searchResult[0].name + '/')
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

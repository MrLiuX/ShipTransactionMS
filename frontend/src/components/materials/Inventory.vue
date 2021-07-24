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
            <!--<el-table-column label="操作" width="250px">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="primary"
                  plain
                  @click="storageDialogVisible = true"
                  >申请采购入库</el-button
                >
                <el-button
                  size="mini"
                  type="success"
                  plain
                  @click="UnStorage(scope.$index, scope.row)"
                  >申请出库</el-button
                >
              </template>
            </el-table-column>-->
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
        ><el-button type="primary" plain @click="storageDialogVisible = true"
          >申请采购入库</el-button
        >
        <el-button
          type="success"
          plain
          @click="UnStorage(scope.$index, scope.row)"
          >申请出库</el-button
        >
      </span>
    </el-dialog>

    <!--<el-dialog title="购置入库申请" :visible.sync="storageDialogVisible">
      <el-form :model="storageForm">
        <el-form-item label="物料名称" :label-width="formLabelWidth">
          <el-select v-model="storageForm.Material" placeholder="请选择物料">
            <el-option
              :label="dData.name"
              :value="dData.name"
              v-for="dData in inventoryListData"
              :key="dData.name"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="申请人" :label-width="formLabelWidth">
          <el-input
            v-model="storageForm.applicant"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="申请数量" :label-width="formLabelWidth">
          <el-input-number
            v-model="storageForm.applicationsQuantity"
            :min="1"
            :max="1000000"
            label="申请数量"
          ></el-input-number>
        </el-form-item>
        <el-form-item label="供应商" :label-width="formLabelWidth">
          <el-input
            v-model="storageForm.suppliers"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="订单ID" :label-width="formLabelWidth">
          <el-input v-model="storageForm.orderId" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="storageDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="Storage">确 定</el-button>
      </div>
    </el-dialog>-->

    <el-dialog title="购置入库申请" :visible.sync="storageDialogVisible">
      <el-form :model="storageForm">
        <el-form-item label="申请人" :label-width="formLabelWidth">
          <el-input
            v-model="storageForm.applicant"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="申请数量" :label-width="formLabelWidth">
          <el-input-number
            v-model="storageForm.applicationsQuantity"
            :min="1"
            :max="1000000"
            label="申请数量"
          ></el-input-number>
        </el-form-item>
        <el-form-item label="供应商" :label-width="formLabelWidth">
          <el-input
            v-model="storageForm.suppliers"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="订单ID" :label-width="formLabelWidth">
          <el-input v-model="storageForm.orderId" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="storageDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="Storage">确 定</el-button>
      </div>
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
      storageDialogVisible: false,
      UnstorageDialogVisible: false,
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
      },
      storageForm: {
        applicant: '',
        Material: '',
        isAgree: false,
        applicationsQuantity: '',
        OperationType: true,
        suppliers: '',
        orderId: ''
      },
      UnStorageForm: {
        applicant: '',
        Material: '',
        isAgree: false,
        applicationsQuantity: '',
        OperationType: false,
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
      console.log(result)
      if (result.data.name) {
        this.$message.success('添加成功')
        this.addInventoryDialogVisible = false
        window.location.reload()
      }
    },
    deleteInventory() {
      this.$axios.delete('/api/inventorys/' + this.searchResult[0].name + '/')
      this.$message.success('删除成功')
      this.dialogTableVisible = false
      window.location.reload()
    },
    dialogClose() {
      this.searchResult = []
    },
    async Storage(index, row) {
      this.storageForm.Material = this.searchId
      this.searchInventoryDialogVisible = false
      const result = await this.$axios.post(
        '/api/applications/',
        this.storageForm
      )
      if (result.data.Material) {
        const resultToPatch = await this.$axios.get(
          '/api/inventorys/' + this.storageForm.Material + '/'
        )
        var patchForm = {
          inventory:
            resultToPatch.data.inventory +
            this.storageForm.applicationsQuantity,
          accumulativeStorage:
            resultToPatch.data.accumulativeStorage +
            this.storageForm.applicationsQuantity
        }
        this.$axios.patch(
          '/api/inventorys/' + this.storageForm.Material + '/',
          patchForm
        )
        window.location.reload()
        this.$message.success('添加成功')
        this.storageDialogVisible = false
      }
    },
    UnStorage(index, row) {}
  }
}
</script>

<style scoped>
.search-input {
  width: 20rem;
  padding: 1rem;
}
</style>

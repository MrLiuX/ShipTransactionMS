<template>
  <div>
    <el-dialog title="购置入库申请" :visible.sync="storageDialogVisible">
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
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      storageDialogVisible: true,
      storageForm: {
        applicant: '',
        Material: '',
        isAgree: false,
        applicationsQuantity: '',
        OperationType: true,
        suppliers: '',
        orderId: ''
      },
      inventoryListData: []
    }
  },
  created() {
    this.getInventoryList()
  },
  methods: {
    async getInventoryList() {
      const { data: result } = await this.$axios.get('/api/inventorys/')
      this.inventoryListData = result
    },
    async Storage(index, row) {
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
    }
  }
}
</script>

<style scoped></style>

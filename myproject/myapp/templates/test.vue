<template>
    <div>
      <el-row :gutter="15">
        <el-form ref="elForm" :model="formData" :rules="rules" size="medium" label-width="100px">
          <el-col :span="10">
            <el-form-item label="单行文本" prop="field102">
              <el-input v-model="formData.field102" placeholder="请输入单行文本" clearable :style="{width: '100%'}">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="4">
            <el-form-item label="按钮" prop="field104">
              <el-button type="primary" icon="el-icon-search" size="medium"> 主要按钮 </el-button>
            </el-form-item>
          </el-col>
          <el-col :span="5">
            <el-form-item label="按钮" prop="field103">
              <el-button type="primary" icon="el-icon-search" size="medium"> 主要按钮 </el-button>
            </el-form-item>
          </el-col>
          <el-col :span="22">
            <el-form-item label="单行文本" prop="field105">
              <el-input v-model="formData.field105" placeholder="请输入单行文本" clearable :style="{width: '100%'}">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="22">
            <el-form-item label="单行文本" prop="field106">
              <el-input v-model="formData.field106" placeholder="请输入单行文本" clearable :style="{width: '100%'}">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="22">
            <el-form-item label="单行文本" prop="field107">
              <el-input v-model="formData.field107" placeholder="请输入单行文本" clearable :style="{width: '100%'}">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="22">
            <el-form-item label="单行文本" prop="field108">
              <el-input v-model="formData.field108" placeholder="请输入单行文本" clearable :style="{width: '100%'}">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item size="large">
              <el-button type="primary" @click="submitForm">提交</el-button>
              <el-button @click="resetForm">重置</el-button>
            </el-form-item>
          </el-col>
        </el-form>
      </el-row>
    </div>
  </template>
  <script>
  export default {
    components: {},
    props: [],
    data() {
      return {
        formData: {
          field102: undefined,
          field104: undefined,
          field103: undefined,
          field105: undefined,
          field106: undefined,
          field107: undefined,
          field108: undefined,
        },
        rules: {
          field102: [{
            required: true,
            message: '请输入单行文本',
            trigger: 'blur'
          }],
          field105: [{
            required: true,
            message: '请输入单行文本',
            trigger: 'blur'
          }],
          field106: [{
            required: true,
            message: '请输入单行文本',
            trigger: 'blur'
          }],
          field107: [{
            required: true,
            message: '请输入单行文本',
            trigger: 'blur'
          }],
          field108: [{
            required: true,
            message: '请输入单行文本',
            trigger: 'blur'
          }],
        },
      }
    },
    computed: {},
    watch: {},
    created() {},
    mounted() {},
    methods: {
      submitForm() {
        this.$refs['elForm'].validate(valid => {
          if (!valid) return
          // TODO 提交表单
        })
      },
      resetForm() {
        this.$refs['elForm'].resetFields()
      },
    }
  }
  
  </script>
  <style>
  </style>
  
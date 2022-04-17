<!--
 * @Author: YJR-1100
 * @Date: 2022-04-13 10:34:12
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-17 16:50:46
 * @FilePath: \webformanager\src\views\innerperson.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="yjr-innerpersoncontant">
    <div class="backimg"></div>
    <div class="backmask"></div>
    <div class="tablebody">
      <template>
        <el-table :data="peoplelist" border class="mytable" :header-cell-style="{ 'text-align': 'center' }" :cell-style="{ 'text-align': 'center' }">
          <el-table-column prop="uid" label="编号" width="50"></el-table-column>
          <el-table-column fixed prop="uname" label="姓名" width="120"> </el-table-column>
          <el-table-column prop="nickname" label="昵称" width="150" show-overflow-tooltip> </el-table-column>
          <el-table-column prop="uphonenum" label="手机号" width="130"> </el-table-column>
          <el-table-column prop="schoolid" label="学号" width="130"> </el-table-column>
          <el-table-column prop="profassionclass" label="专业班级" width="150"> </el-table-column>
          <el-table-column
            prop="isinsider"
            label="状态"
            width="100"
            :filters="[
              { text: '待审核', value: 2 },
              { text: '审核通过', value: 1 }
            ]"
            :filter-method="filterTag"
            filter-placement="bottom-end"
          >
            <template slot-scope="scope">
              <el-tag :type="scope.row.isinsider === 2 ? 'info' : 'primary'" disable-transitions>{{ scope.row.isinsider === 2 ? '待审核' : '通过' }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="操作" width="150">
            <template slot-scope="scope">
              <el-button v-if="scope.row.isinsider === 2" type="success" size="mini" @click="handlechange(scope.$index, scope.row, 1)">通过</el-button>
              <el-button v-if="scope.row.isinsider === 2" type="warning" size="mini" @click="handlechange(scope.$index, scope.row, -1)">拒绝</el-button>
              <el-button v-else size="mini" type="danger" @click="handlechange(scope.$index, scope.row, 0)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 'yjr-innerperson',
  props: ['tooken', 'datatooken'],
  data() {
    return {
      peoplelist: []
    }
  },
  methods: {
    async handlechange(index, row, status) {
      console.log(index, row)
      const postdata = {
        uid: row.uid,
        status: status
      }
      const { data } = await this.$http.post('/manager/updateinnerpersonstate', postdata)
      // console.log(data)
      if (data.code === 0) {
        this.$message.error(data.msg)
      } else {
        this.$message({
          message: data.msg,
          type: 'success'
        })
      }

      this.getpeoplelist(JSON.parse(localStorage.getItem('manager')).m2org)
    },
    filterTag(value, row) {
      console.log(row)
      return row.isinsider === value
    },
    async getpeoplelist(orgid) {
      const { data } = await this.$http.get('/manager/getpeople', {
        params: {
          orgid: orgid
        }
      })
      this.peoplelist = data.responsedata
      if (data.code === -1) {
        this.$message.error('数据拉取失败')
      }
    }
  },
  created() {
    this.getpeoplelist(JSON.parse(localStorage.getItem('manager')).m2org)
    console.log(' --')
  }
}
</script>

<style lang="less" scoped>
.yjr-innerpersoncontant {
  height: 100%;
  width: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  .backmask {
    position: absolute;
    z-index: -98;
    height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.5);
  }
  .backimg {
    position: absolute;
    z-index: -99;
    height: 100%;
    width: 100%;
    background-image: url('@/assets/loginbackimg3.jpg');
    background-size: 100% 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: blur(2px);
  }
  .tablebody {
    padding: 50px 50px;
    width: auto;
    max-width: 80%;
    position: absolute;
  }
}
</style>

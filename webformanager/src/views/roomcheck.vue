<!--
 * @Author: YJR-1100
 * @Date: 2022-04-13 10:31:23
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-18 21:12:30
 * @FilePath: \webformanager\src\views\roomcheck.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="yjr-roomcheckcontant">
    <div class="backimg"></div>
    <div class="backmask"></div>
    <div class="tablebody">
      <template>
        <el-table :data="orderlist" border class="mytable" :header-cell-style="{ 'text-align': 'center' }" :cell-style="{ 'text-align': 'center' }" :default-sort="{ prop: 'ordertime', order: 'descending' }">
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="申请人">
                  <span>{{ props.row.username }}</span>
                </el-form-item>
                <el-form-item label="申请时间">
                  <span>{{ props.row.ordertime }}</span>
                </el-form-item>
                <el-form-item label="学  号">
                  <span>{{ props.row.schoolid }}</span>
                </el-form-item>
                <el-form-item label="使用时间">
                  <span>{{ props.row.usingtime }}</span>
                </el-form-item>
                <el-form-item label="手机号">
                  <span>{{ props.row.uphonenum }}</span>
                </el-form-item>
                <el-form-item label="审核时间">
                  <span>{{ props.row.ochecktime ? props.row.ochecktime : '待审核' }}</span>
                </el-form-item>
                <el-form-item label="教室名称">
                  <span>{{ props.row.roomname }}</span>
                </el-form-item>
                <el-form-item label="审核人员">
                  <span>{{ props.row.checkername ? props.row.checkername : '待审核' }}</span>
                </el-form-item>
                <el-form-item label="教室位置">
                  <span>{{ props.row.address }}</span>
                </el-form-item>
                <el-form-item label="拒绝理由">
                  <span>{{ props.row.rejectreasion ? props.row.rejectreasion : '无' }}</span>
                </el-form-item>
                <el-form-item label="教室用途">
                  <span>{{ props.row.roomusage }}</span>
                </el-form-item>
                <el-form-item label="签字图片">
                  <span v-if="props.row.userinner === 1">内部人员无需签字</span>
                  <span v-else>
                    <el-image v-for="imgurl in props.row.autograph" :key="imgurl" :src="imgurl" alt="" class="autographimg" :preview-src-list="props.row.autograph"></el-image>
                  </span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column prop="oid" label="编号" width="50"></el-table-column>
          <el-table-column prop="username" label="申请人" width="120" show-overflow-tooltip> </el-table-column>
          <el-table-column prop="roomname" label="教室名称" width="150" show-overflow-tooltip :filters="roomnamefilters" :filter-method="roomnamefilterHandler"> </el-table-column>
          <el-table-column sortable :sort-method="sortordertime" prop="ordertime" label="申请时间" width="150"> </el-table-column>
          <el-table-column sortable prop="usingtime" label="使用时间" width="200"> </el-table-column>
          <el-table-column
            prop="status"
            label="状态"
            width="100"
            :filters="[
              { text: '待审核', value: -1 },
              { text: '通过', value: 1 },
              { text: '不通过', value: 0 }
            ]"
            :filter-method="filterTag"
            filter-placement="bottom-end"
          >
            <template slot-scope="scope">
              <el-tag v-if="scope.row.status === 1" type="success" disable-transitions>通过</el-tag>
              <el-tag v-else-if="scope.row.status === -1" type="info" disable-transitions>待审核</el-tag>
              <el-tag v-else type="danger" disable-transitions>不通过</el-tag>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="操作" width="150">
            <template slot-scope="scope">
              <el-button type="success" size="mini" @click="handlechange(scope.$index, scope.row, 1)">通过</el-button>
              <el-button size="mini" type="danger" @click="handlechange(scope.$index, scope.row, 0)">拒绝</el-button>
            </template>
          </el-table-column>
        </el-table>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 'yjr-roomcheck',
  props: ['tooken', 'datatooken'],
  data() {
    return {
      orderlist: [],
      roomnamefilters: []
    }
  },
  methods: {
    roomnamefilterHandler(value, row) {
      return row.roomname === value
    },
    sortordertime(a, b) {
      a = a.ordertime
      b = b.ordertime
      const dataa = new Date(a.replace(/-/g, '/'))
      const datab = new Date(b.replace(/-/g, '/'))
      return dataa - datab
    },
    async handlechange(index, row, status) {
      console.log(index, row)
      const postdata = {
        oid: row.oid,
        status: status,
        checker_id: JSON.parse(localStorage.getItem('manager')).mid
      }
      if (status === 1) {
        const { data } = await this.$http.post('/orderitems/checkorder', postdata)
        console.log(data)
        this.$message({
          message: data.msg,
          type: 'success'
        })
      } else {
        const { value } = await this.$prompt('请输入拒绝原因', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        }).catch()
        const reason = value
        console.log(reason)
        if (!reason) {
          this.$message.error('你必须输入字符')
        } else {
          postdata.value = reason
          const { data } = await this.$http.post('/orderitems/checkorder', postdata)
          console.log(data)
          this.$message({
            message: data.msg,
            type: 'success'
          })
        }
      }
      this.getorderlist(JSON.parse(localStorage.getItem('manager')).m2org)
    },
    filterTag(value, row) {
      return row.status === value
    },
    async getorderlist(orgid) {
      const { data } = await this.$http.post('/orderitems/managergetorder', {
        orgid: orgid
      })
      this.orderlist = data.responsedata
      this.orderlist.forEach((order) => {
        const graphlist = order.autograph.split(';')
        if (graphlist[0] === 1) order.autograph = graphlist[1]
        else if (graphlist[0] === 0) order.autograph = graphlist[1]
        else {
          order.autograph = graphlist
        }
      })
      // console.log(data.responsedata)
      if (data.code === -1) {
        this.$message.error('数据拉取失败')
      }
    },
    async getallroom(orgid) {
      const { data } = await this.$http.get('/room/getrooms', {
        params: { orgid: orgid }
      })
      data.responsedata.forEach((element) => {
        this.roomnamefilters.push({ text: element.name, value: element.name })
      })
    }
  },
  created() {
    this.getorderlist(JSON.parse(localStorage.getItem('manager')).m2org)
    this.getallroom(JSON.parse(localStorage.getItem('manager')).m2org)
  }
}
</script>

<style lang="less" scoped>
.yjr-roomcheckcontant {
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
    background-image: url('@/assets/loginbackimg.jpg');
    background-size: 100% 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: blur(2px);
  }
  .tablebody {
    padding: 30px 30px;
    width: auto;
    max-width: 75%;
    // position: absolute;
    .demo-table-expand {
      font-size: 0;
      width: 100%;
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      /deep/.el-form-item {
        display: flex;
        margin-right: 0;
        margin-bottom: 0;
        width: 50%;
        .el-form-item__label {
          display: block;
          font-weight: 600;
          text-align: right;
          width: 90px;
          flex-shrink: 0;
          color: #95b2db !important;
        }
        span {
          display: block;
        }
        .autographimg {
          width: 100px;
          height: 100px;
          border: #95b2db 1 solid;
          margin: 5px 5px 0 0;
        }
      }
    }
  }
}
</style>

<!--
 * @Author: YJR-1100
 * @Date: 2022-04-17 13:46:25
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-17 23:25:55
 * @FilePath: \webformanager\src\views\organdmanagerset.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->
<template>
  <div class="yjr-organdmanagercontant">
    <div class="backimg"></div>
    <div class="backmask"></div>
    <div class="yjr-main">
      <div class="orgtablebody">
        <template>
          <h1>组织管理</h1>
          <el-table :data="orglist" border class="mytable" :header-cell-style="{ 'text-align': 'center' }" :cell-style="{ 'text-align': 'center' }">
            <el-table-column prop="orgid" label="编号" width="50"></el-table-column>
            <el-table-column prop="orgname" label="组织名称" width="150" show-overflow-tooltip> </el-table-column>
            <el-table-column label="操作" width="120">
              <template slot-scope="scope">
                <el-button size="mini" type="danger" @click="handlechange(scope.row, 0)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-button icon="el-icon-circle-plus-outline" type="text" @click="open" class="addorgbtn">点击添加组织</el-button>
        </template>
      </div>
      <div class="managertablebody">
        <template>
          <h1>管理员</h1>
          <el-table :data="managerlist" border class="mytable" :header-cell-style="{ 'text-align': 'center' }" :cell-style="{ 'text-align': 'center' }">
            <el-table-column prop="mid" label="编号" width="50"></el-table-column>
            <el-table-column prop="mname" label="姓名" width="120"> </el-table-column>
            <el-table-column prop="mphonenum" label="手机号" width="120"> </el-table-column>
            <el-table-column prop="mpassword" label="密码" width="120"> </el-table-column>
            <el-table-column prop="orgname" label="所属组织" width="150" show-overflow-tooltip> </el-table-column>
            <el-table-column label="操作" width="180">
              <template slot-scope="scope">
                <el-button type="primary" size="mini" @click="handlechange(scope.row, 2)">编辑</el-button>
                <el-button size="mini" type="danger" @click="handlechange(scope.row, 1)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <button @click="handlechange({}, 2)" class="addmanagerbtn"><i class="el-icon-circle-plus-outline"></i>点击添加管理员</button>
        </template>
      </div>
    </div>
    <!-- 管理员信息编辑 -->
    <div class="managerdetailcontant" v-show="isshowdetail" @click.self="clickmask">
      <div class="managerdetails">
        <div>
          <span>管理员姓名</span>
          <input type="text" placeholder="请输入内容" v-model.trim="managerdetail.mname" />
        </div>
        <div>
          <span>所属组织</span>
          <template>
            <el-select v-model="managerdetail.orgname" placeholder="请选择组织" class="selectttt">
              <el-option v-for="org in orglist" :key="org.orgid" :label="org.orgname" :value="org.orgname"> </el-option>
            </el-select>
          </template>
        </div>
        <div>
          <span>手机号</span>
          <input type="text" placeholder="请输入内容" v-model.trim="managerdetail.mphonenum" />
        </div>
        <div>
          <span>密码</span>
          <input type="text" placeholder="请输入内容" v-model.trim="managerdetail.mpassword" />
        </div>
        <div class="submitbtn">
          <el-button @click="clickmask" type="primary" plain style="font-size: 16px; padding: 0; line-height: 35px; height: 35px; width: 80px">关闭</el-button>
          <el-button @click="submitbtn" type="success" plain style="font-size: 16px; padding: 0; line-height: 35px; height: 35px; width: 80px">提交</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'yjr-organdmanager',
  props: ['tooken', 'datatooken'],
  data() {
    return {
      orglist: [],
      managerlist: [],
      savetooken: null,
      isshowdetail: false,
      managerdetail: {
        maname: null,
        mphonenum: null,
        orgname: null,
        mpassword: null,
        m2org: null,
        mid: null
      }
    }
  },
  created() {
    this.getallorg()
    this.getallmanager(this.tooken)
    this.savetooken = this.tooken
    if (!this.tooken) {
      localStorage.removeItem('manager')
      this.$router.replace('/login')
    }
  },
  methods: {
    async open() {
      const { value } = await this.$prompt('请输入组织名称', '添加组织', {
        confirmButtonText: '确定',
        cancelButtonText: '取消'
      }).catch()
      const reason = value
      console.log(reason)
      if (!reason) {
        this.$message.error('你必须输入字符')
      } else {
        const postdata = {
          orgname: reason,
          tooken: this.tooken,
          mid: JSON.parse(localStorage.getItem('manager')).mid
        }
        const { data } = await this.$http.post('/org/addorg', postdata)
        console.log(data)
        if (data.code === 1) {
          this.$message({
            message: data.msg,
            type: 'success'
          })
          this.getallorg()
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    clickmask() {
      this.isshowdetail = false
      this.managerdetail = {}
    },
    submitbtn() {
      const mPattern = /^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$/

      if (!this.managerdetail.mname || !this.managerdetail.mpassword || !this.managerdetail.mphonenum || !this.managerdetail.orgname) {
        this.$message.error('请输入完整的管理员信息')
      } else if (!mPattern.test(this.managerdetail.mphonenum)) {
        this.$message.error('手机号格式错误')
      } else {
        const postdata = this.managerdetail
        postdata.tooken = this.tooken
        postdata.optmid = JSON.parse(localStorage.getItem('manager')).mid
        if (this.managerdetail.mid) {
          postdata.isnew = false
        } else {
          postdata.isnew = true
          this.orglist.every((org) => {
            if (org.orgname === this.managerdetail.orgname) {
              postdata.m2org = org.orgid
            }
            return true
          })
        }
        this.$http.post('/manager/addmanager', postdata).then((result) => {
          console.log(result)
          if (result.data.code === 1) {
            this.$message.success(result.data.msg)
            this.getallmanager(this.tooken)
          } else {
            this.$message.error(result.data.msg)
          }
        })
        this.isshowdetail = false
        this.managerdetail = {}
      }
    },
    async handlechange(row, status) {
      try {
        const managertest = localStorage.getItem('manager')
        if (!managertest) {
          this.$message.error('登录过期')
          this.$router.replace('/login')
        }
      } catch {
        this.$message.error('登录过期')
        localStorage.removeItem('manager')
        this.$router.replace('/login')
      }
      if (status === 0) {
        const res = await this.$confirm('此操作将永久删除该组织和其成员, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
        if (res) {
          const postdata = {
            orgid: row.orgid,
            tooken: this.tooken,
            mid: JSON.parse(localStorage.getItem('manager')).mid
          }
          const { data } = await this.$http.post('/org/rmorg', postdata)
          if (data.code === 1) {
            this.$message({
              message: data.msg,
              type: 'success'
            })
            this.getallorg()
            this.getallmanager(this.tooken)
          } else {
            this.$message.error(data.msg)
          }
        }
      } else if (status === 1) {
        // 删除管理员
        const res = await this.$confirm('此操作将永久删除该组织和其成员, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
        if (res) {
          const postdata = {
            mid: row.mid,
            tooken: this.tooken,
            optmid: JSON.parse(localStorage.getItem('manager')).mid,
            optm2org: JSON.parse(localStorage.getItem('manager')).m2org
          }
          // console.log(postdata)
          const { data } = await this.$http.post('/manager/rmmanager', postdata)
          if (data.code === 1) {
            this.$message({
              message: data.msg,
              type: 'success'
            })
            this.getallmanager(this.tooken)
          } else {
            this.$message.error(data.msg)
          }
        }
      } else if (status === 2) {
        this.isshowdetail = true
        this.managerdetail = row
      }
    },
    async getallorg() {
      const { data } = await this.$http.get('/org/getallorg')
      // console.log(data)
      if (data.code === 0) {
        this.$message.error(data.msg)
        localStorage.removeItem('manager')
        this.$router.replace('/login')
      } else {
        this.orglist = data.responsedata
      }
    },
    async getallmanager(tooken) {
      const { data } = await this.$http.post('/manager/getallmanager', {
        tooken: tooken,
        mid: JSON.parse(localStorage.getItem('manager')).mid
      })
      // console.log(data)
      if (data.code === 0) {
        this.$message.error(data.msg)
        localStorage.removeItem('manager')
        this.$router.replace('/login')
      } else {
        this.managerlist = data.responsedata
      }
    }
  }
}
</script>

<style lang="less" scoped>
.yjr-organdmanagercontant {
  min-height: 100%;
  width: 100%;
  position: relative;
  .backmask {
    position: absolute;
    z-index: -98;
    min-height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.5);
  }
  .backimg {
    position: absolute;
    z-index: -99;
    min-height: 100%;
    width: 100%;
    background-image: url('@/assets/loginbackimg2.jpg');
    background-size: 100% 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: blur(2px);
  }
  .yjr-main {
    display: flex;
    justify-content: space-around;
    width: 90vw;
    margin: 0 auto;
    padding: 30px 30px;
    width: auto;
    max-width: 85%;
    h1 {
      display: block;
      background-color: #fff;
      margin: 0;
      padding: 20px;
      color: #909399;
      font-weight: 600;
      text-align: center;
      font-size: 1.5vw;
    }
    .addmanagerbtn {
      width: 100%;
      background-color: #fff;
      border-radius: 0;
      height: 40px;
      padding: 0;
      color: #909eff;
      border: 0;
      margin: 0;
      font-size: 14px;
      &:focus {
        outline: 0;
      }
    }
    /deep/.addorgbtn {
      width: 100%;
      background-color: #fff;
      border-radius: 0;
      &:focus {
        outline: 0;
      }
    }
  }
  .managerdetailcontant {
    position: absolute;
    z-index: 1;
    top: 0;
    min-height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    .managerdetails {
      display: flex;
      position: relative;
      flex-direction: column;
      background: rgba(249, 249, 249, 0.9);
      box-shadow: 0 0 8px rgb(224, 223, 223);
      border-radius: 10px;
      padding: 20px;
      margin: 100px 0;
      width: 35vw;
      min-width: 480px;
      overflow: auto;
      height: 290px;
      .submitbtn {
        display: flex;
        justify-content: right;
      }
      div {
        display: flex;
        flex-direction: row;
        margin: 5px 0;
        align-items: center;
        span {
          display: block;
          margin-right: 10px;
          font-size: 18px;
          font-weight: 600;
          width: 90px;
          text-align: right;
          flex-shrink: 0;
        }
        /deep/.selectttt {
          width: 100%;
          font-size: 16px;
        }
        input {
          :placeholder-shown {
            color: #909399;
          }
          font-size: 16px;
          display: block;
          resize: vertical;
          padding: 5px 15px;
          line-height: 1.5;
          width: 100%;
          color: #606266;
          border: 1px solid #dcdfe6;
          background-color: #fbfbfb;
          border-radius: 4px;
          transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
          overflow-wrap: wrap;
          &:focus {
            outline: 0;
            border: 1px solid #919abc;
          }
        }
        /deep/.el-textarea__inner {
          margin: 0;
          font-size: 16px;
          background-color: #fbfbfb;

          &:focus {
            border: 1px solid #919abc;
          }
        }
        .lables {
          display: flex;
          flex-wrap: wrap;
          flex-direction: row;
          flex-shrink: 0;
          width: 40vw;
          /deep/ .lable {
            width: 134px;
            margin: 5px;
          }
          .selecttime {
            position: relative;
            /deep/.eladdbtn {
              width: 134px;
              height: 30px;
              margin: 5px;
              line-height: 30px;
              padding: 0 20px;
              // margin: 10px 0.5vw 0 0;
              &:focus {
                outline: 0;
              }
            }
            /deep/.select {
              flex-direction: column;
              display: flex;
              border-radius: 5px;
            }
          }
        }
      }
    }
  }
  input::-webkit-input-placeholder {
    color: #c0c9da;
  }
  input::-moz-placeholder {
    /* Mozilla Firefox 19+ */
    color: #c0c9da;
  }
  input:-moz-placeholder {
    /* Mozilla Firefox 4 to 18 */
    color: #c0c9da;
  }
  input:-ms-input-placeholder {
    /* Internet Explorer 10-11 */
    color: #c0c9da;
  }
}
</style>

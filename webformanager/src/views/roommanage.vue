<!--
 * @Author: YJR-1100
 * @Date: 2022-04-13 10:35:23
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-19 22:42:31
 * @FilePath: \webformanager\src\views\roommanage.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.

-->
<template>
  <div class="yjr-roommanagecontant">
    <div class="backimg"></div>
    <div class="backmask"></div>
    <!-- 教室详细信息展示 -->
    <div class="roomdetailcontant" v-show="isshowdetail" @click.self="clickmask">
      <div class="roomdetails">
        <div>
          <span>教室名称</span>
          <input type="text" v-model="roomdetail.name" />
        </div>
        <div>
          <span>教室地址</span>
          <input type="text" v-model="roomdetail.adress" />
        </div>
        <div>
          <span>教室描述</span>
          <el-input type="textarea" autosize placeholder="请输入内容" v-model="roomdetail.describe"> </el-input>
        </div>
        <div>
          <span>教室图片</span>
          <div class="roomimages">
            <div class="imgdiv" v-for="item in roomdetail.imageurl" :key="item">
              <img :src="item" alt="教室详情图片" />
              <div class="hovermask" @click="deletimg(item)">
                <i class="el-icon-delete"></i>
              </div>
            </div>
            <div class="imgdiv">
              <div class="addhovermask">
                <input ref="hiddenuplode" type="file" name="file" multiple style="display: none" @change="upload" />
                <i class="el-icon-circle-plus-outline" @click="uploadfile"></i>
                <p>只能上传jpg/png文件，且不超过500kb</p>
              </div>
            </div>
          </div>
        </div>
        <div>
          <span>可借时间</span>
          <div class="lables">
            <el-tag :key="tag" v-for="tag in roomdetail.rcanbeusetimes" closable :disable-transitions="false" @close="handleClose(tag)" class="lable">
              {{ tag }}
            </el-tag>
            <div class="selecttime">
              <el-popover placement="bottom" width="470" v-model="visible" class="select">
                <div>
                  <el-time-select
                    placeholder="起始时间"
                    v-model="startTime"
                    :picker-options="{
                      start: '08:00',
                      step: '00:15',
                      end: '22:30'
                    }"
                  >
                  </el-time-select>
                  <el-time-select
                    placeholder="结束时间"
                    v-model="endTime"
                    :picker-options="{
                      start: '08:00',
                      step: '00:15',
                      end: '22:30',
                      minTime: startTime
                    }"
                  ></el-time-select>
                </div>
                <div id="addtimebtn" style="text-align: right; margin-top: 10px">
                  <el-button @click="selecttimebtn(false)" type="primary" plain style="padding: 0; line-height: 30px; height: 30px; width: 50px">取消</el-button>
                  <el-button @click="selecttimebtn(true)" type="success" plain style="padding: 0; line-height: 30px; height: 30px; width: 50px">确定</el-button>
                </div>
                <el-button slot="reference" icon="el-icon-circle-plus-outline" type="primary" class="eladdbtn">添加</el-button>
              </el-popover>
            </div>
          </div>
        </div>
        <div class="submitbtn">
          <el-button @click="submitbtn(false)" type="primary" plain style="font-size: 16px; padding: 0; line-height: 35px; height: 35px; width: 80px">关闭</el-button>
          <el-button @click="submitbtn(true)" type="success" plain style="font-size: 16px; padding: 0; line-height: 35px; height: 35px; width: 80px">提交</el-button>
        </div>
      </div>
    </div>
    <div class="roomlists">
      <div class="roomitem" v-for="(item, index) in roomlist" :key="item.rid" @click="showdetails(index)">
        <img :src="item.imageurl[0]" alt="" class="roomimg" :id="'roomimg' + item.rid" />
        <label :for="'roomimg' + item.rid">{{ item.name }}</label>
      </div>
    </div>
    <!-- 添加教室的按钮 -->
    <div class="addbtn" @click="addnewroombtn">
      <p class="iconfont icon-shizijiahao3"></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'yjr-roommanage',
  props: ['tooken', 'datatooken'],
  data() {
    return {
      visible: false,
      isshowdetail: false,
      roomlist: [],
      startTime: '',
      endTime: '',
      roomdetail: {
        rid: '',
        orgid: '',
        name: '',
        adress: '',
        describe: '',
        imageurl: [],
        rcanbeusetimes: []
      }
    }
  },

  created() {
    // 发送请求得到该管理者管理的所有教室

    this.getallroom(JSON.parse(localStorage.getItem('manager')).m2org)
  },
  methods: {
    deletimg(url) {
      this.roomdetail.imageurl.splice(this.roomdetail.imageurl.indexOf(url), 1)
    },
    addnewroombtn() {
      this.isshowdetail = true
      this.roomdetail.imageurl = []
      this.roomdetail.rcanbeusetimes = []
      this.roomdetail.rid = ''
      this.roomdetail.orgid = JSON.parse(localStorage.getItem('manager')).m2org
      this.roomdetail.name = ''
      this.roomdetail.adress = ''
      this.roomdetail.describe = ''
      this.roomdetail.isnewroom = 1
    },
    clickmask() {
      this.isshowdetail = false
    },
    handleClose(i) {
      this.roomdetail.rcanbeusetimes.splice(this.roomdetail.rcanbeusetimes.indexOf(i), 1)
    },
    submitbtn(status) {
      if (status) {
        const postdata = this.roomdetail
        console.log(postdata)
        this.$http.post('/manager/updaterooms', postdata).then((result) => {
          console.log(result)
          if (result.data.code === 1) {
            this.$message({
              message: result.data.msg,
              type: 'success'
            })
            this.getallroom(JSON.parse(localStorage.getItem('manager')).m2org)
          } else {
            if (postdata.isnewroom) {
              this.$message.error('添加失败')
            } else {
              this.$message.error('修改失败')
            }
          }
        })
      }
      this.isshowdetail = false
      this.roomdetail = {}
    },
    selecttimebtn(status) {
      const value = this.startTime + '-' + this.endTime
      if (status && !this.roomdetail.rcanbeusetimes.includes(value)) {
        this.roomdetail.rcanbeusetimes.push(value)
      } else if (status) {
        this.$message.error('该时间段已存在')
      }
      this.startTime = this.endTime = ''
      this.visible = false
    },
    upload(e) {
      for (const item of e.target.files) {
        // 正则表达式，判断每个元素的type属性是否为图片形式，如图
        if (!/image\/\w+/.test(item.type)) {
          // 提示只能是图片，return
          alert('只能选择图片')
          return
        } else {
          const fd = new FormData()
          fd.append('file', item)
          this.$http.post('/room/uploadrooomimage', fd).then((result) => {
            console.log(result)
            if (result.data.code === 1) {
              this.$message({
                message: result.data.msg,
                type: 'success'
              })
              this.roomdetail.imageurl.push(result.data.responsedata.imgurl)
            } else {
              this.$message.error('上传出错')
            }
          })
        }
      }
    },
    uploadfile() {
      this.$refs.hiddenuplode.click()
    },
    async getallroom(orgid) {
      const { data } = await this.$http.get('/room/getrooms', {
        params: { orgid: orgid }
      })
      this.roomlist = data.responsedata
    },
    showdetails(index) {
      this.isshowdetail = true
      this.roomdetail = this.roomlist[index]
      this.roomdetail.isnewroom = 0
    }
  }
}
</script>

<style lang="less" scoped>
.yjr-roommanagecontant {
  min-height: 100%;
  width: 100%;
  // position: relative;
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
  .roomlists {
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    position: relative;
    .roomitem {
      display: flex;
      flex-direction: column;
      height: 220px;
      width: 350px;
      background-color: rgba(255, 255, 255, 0.7);
      margin: 10px;
      .roomimg {
        flex: 5;
        display: block;
        height: 190px;
        width: 100%;
      }
      label {
        flex: 2;
        display: block;
        font-size: 1vw;
        text-align: center;
        font-weight: 400;
      }
      &:hover {
        color: #4a567a;
        cursor: pointer;
        label {
          cursor: pointer;
        }
      }
    }
  }
  .addbtn {
    position: fixed;
    bottom: 40px;
    right: 40px;
    background-color: #54648f;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-content: center;
    text-align: center;
    box-shadow: 0 0 15px #616e81;
    p {
      display: block;
      width: 60px;
      height: 60px;
      line-height: 60px;
      border-radius: 50%;
      margin: 0;
      color: #cccdce;
      font-size: 35px;
    }
    &:hover {
      cursor: pointer;
      background-color: #4e67ad;
      p {
        cursor: pointer;
        color: #fff;
      }
    }
  }
  .roomdetailcontant {
    position: absolute;
    z-index: 1;
    min-height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    .roomdetails {
      display: flex;
      position: relative;
      flex-direction: column;
      background: rgba(249, 249, 249, 0.9);
      box-shadow: 0 0 8px rgb(224, 223, 223);
      border-radius: 10px;
      padding: 20px;
      margin: 40px 0;
      width: 48vw;
      overflow: auto;
      height: 79vh;
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
          flex-shrink: 0;
        }
        input {
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
      .roomimages {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        flex-shrink: 0;
        width: 40vw;
        .imgdiv {
          width: 18vw;
          height: 10vw;
          position: relative;
          margin: 10px 1.5vw 0 0;
          border-radius: 10px;
          border: 1px solid #919abc;
          img {
            width: 100%;
            height: 100%;
            border-radius: 10px;
          }
          .hovermask {
            width: 100%;
            height: 100%;
            position: absolute;
            border-radius: 10px;

            i {
              display: none;
              font-size: 2vw;
              color: #fbfbfb;
              margin: 0 auto;
            }

            &:hover {
              background-color: #32353c64;
              cursor: pointer;
              i {
                display: inline-block;
              }
            }
          }
          .addhovermask {
            width: 100%;
            height: 100%;
            position: absolute;
            background-color: #fbfbfb;
            border-radius: 10px;
            flex-direction: column;
            justify-content: center;
            &:hover {
              cursor: pointer;
              i {
                color: rgb(57, 105, 239);
              }
            }
            i {
              font-size: 2.5vw;
              color: #b7d2fc;
              margin: 0 auto;
              &:hover {
                color: rgb(57, 105, 239);
              }
            }
          }
        }
      }
    }
  }
}
</style>

<!--
 * @Author: YJR-1100
 * @Date: 2022-04-17 13:42:16
 * @LastEditors: YJR-1100
 * @LastEditTime: 2022-04-19 23:13:55
 * @FilePath: \webformanager\src\views\wxroomorderset.vue
 * @Description:
 *
 * Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
-->

<template>
  <div class="yjr-wxroomordersetcontant">
    <div class="backimg"></div>
    <div class="backmask"></div>
    <div class="yjr-main">
      <div class="yjr-contant">
        <div class="imagewarp">
          <span> 轮播图片 </span>
          <div class="roomimages">
            <div class="imgdiv" v-for="item in swipimglist" :key="item">
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
        <div class="rulescontant">
          <span>教室预约须知</span>
          <el-input type="textarea" autosize placeholder="请输入内容" v-model="textarea1" @change="ischange = true"> </el-input>
          <div class="tips">在编写预约须知时每条间使用英文的";"封号相隔，建议复制本";"封号，防止出错</div>
          <div class="btnwarp">
            <el-button type="primary" size="mini" @click="handlechange()" :disabled="!ischange" class="myupdatebtn">更新</el-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'yjr-wxroomorderset',
  props: ['tooken', 'datatooken'],
  data() {
    return {
      ischange: false,
      orglist: [],
      swipimglist: [],
      textarea1:
        '1.预约使用各功能教室团体需保持教室清洁卫生，不乱丢纸屑杂物，不携带食品进教室。2.使用教室前，应自行检查设施是否正常，卫生是否整洁，发现问题应及时报告，否则出3.原则上功能室内设备（如投影仪、音响等）需有本馆专业人员在场允许后由本馆人员操4.爱护公物，不得乱涂乱画，损坏设施，不得随便坐在把杆上。严禁穿高跟鞋、钉鞋等进'
    }
  },
  created() {
    if (!this.tooken) {
      localStorage.removeItem('manager')
      this.$router.replace('/login')
    }
    this.getrules()
    this.getswiperimage()
  },
  methods: {
    async handlechange() {
      const postdata = {
        text: this.textarea1.replaceAll('\n', ''),
        tooken: this.tooken,
        mid: JSON.parse(localStorage.getItem('manager')).mid
      }
      const { data } = await this.$http.post('/rule/uploadrule', postdata)
      if (data.code === 1) {
        this.$message({
          message: data.msg,
          type: 'success'
        })
      }
    },
    async deletimg(item) {
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
      const postdata = {
        url: item,
        tooken: this.tooken,
        mid: JSON.parse(localStorage.getItem('manager')).mid
      }
      const { data } = await this.$http.post('/swiper/rmswiperimage', postdata)
      console.log(data)
      console.log(postdata)
      if (data.code === 1) {
        this.$message({
          message: data.msg,
          type: 'success'
        })
        this.getswiperimage()
      } else {
        this.$message.error(data.msg)
      }
    },
    async getswiperimage() {
      const {
        data: { responsedata }
      } = await this.$http.get('/swiper/getswiperimage')
      // console.log(responsedata)
      this.swipimglist = responsedata
    },
    async getrules() {
      const { data } = await this.$http.get('/rule/getrule')
      // console.log(responsedata)
      if (data.code === 1) {
        this.textarea1 = data.responsedata
      } else {
        this.$message.error(data.msg)
      }
    },
    async upload(e) {
      for (const item of e.target.files) {
        // 正则表达式，判断每个元素的type属性是否为图片形式，如图
        if (!/image\/\w+/.test(item.type)) {
          // 提示只能是图片，return
          alert('只能选择图片')
          return
        } else {
          const fd = new FormData()
          fd.append('file', item)
          const { data } = await this.$http.post('/swiper/uploadswiperimage', fd)
          console.log(data)
          if (data.code === 1) {
            this.$message({
              message: data.msg,
              type: 'success'
            })
            this.getswiperimage()
          } else {
            this.$message.error('上传出错')
          }
        }
      }
    },
    uploadfile() {
      this.$refs.hiddenuplode.click()
    }
  }
}
</script>

<style lang="less" scoped>
.yjr-wxroomordersetcontant {
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
    width: 100%;
    padding: 40px 0 0 0;
    .yjr-contant {
      width: 90vw;
      display: flex;
      justify-content: space-around;
      border-radius: 10px;
      width: 90vw;
      margin: 0 auto;
      padding: 30px 30px;
      max-width: 85%;
      background-color: #fff;
      span {
        display: block;
        font-size: 20px;
        font-weight: 600;
        flex-shrink: 0;
        width: 100%;
        text-align: center;
      }
      .imagewarp {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 40vw;
        .roomimages {
          display: flex;
          flex-wrap: wrap;
          flex-direction: row;
          flex-shrink: 0;
          justify-content: space-around;
          width: 40vw;
          .imgdiv {
            width: 18vw;
            height: 10vw;
            display: flex;
            position: relative;
            margin: 10px 0 0 0;
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
              display: flex;
              justify-content: center;
              align-items: center;
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
              display: flex;
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
                text-align: center;
                &:hover {
                  color: rgb(57, 105, 239);
                }
              }
              p {
                text-align: center;
              }
            }
          }
        }
      }
      .rulescontant {
        width: 20vw;
        .tips {
          color: #c1c1c1;
          margin: 5px 3px;
        }
        .btnwarp {
          display: flex;
          justify-content: right;
          button {
            width: 70px;
          }
        }
      }
    }
  }
}
</style>

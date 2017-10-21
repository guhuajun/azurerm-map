<style scoped>
.layout {
  background: #f5f7f9;
  position: relative;
  overflow: hidden;
}

.layout-logo {
  color: #f5f7f9;
  font-size: 2vw;
}

.layout-breadcrumb {
  padding: 10px 15px 0;
}

.layout-content {
  min-height: 200px;
  margin: 15px;
  overflow: hidden;
  background: #fff;
  border-radius: 4px;
}

.layout-content-main {
  padding: 10px;
}

.layout-copy {
  text-align: center;
  padding: 10px 0 20px;
  color: #9ea7b4;
}

.layout-menu-left {
  background: #464c5b;
}

.layout-header {
  height: 60px;
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}

.layout-logo-left {
  width: 90%;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  margin: 15px auto;
}

.layout-ceiling-main a {
  color: #9ba7b5;
}

.layout-hide-text .layout-text {
  display: none;
}

.ivu-col {
  transition: width 0.2s ease-in-out;
}
</style>
<template>
    <div class="layout" :class="{'layout-hide-text': spanLeft < 5}">
        <Row type="flex">
            <Col :span="spanLeft" class="layout-menu-left">
            <div class="layout-logo">AzureRM MAP</div>
            </Col>
            <Col :span="spanRight">
            <div class="layout-header">
                <Button type="text" @click="toggleClick">
                    <Icon type="navicon" size="32"></Icon>
                </Button>
            </div>
            <div class="layout-breadcrumb">
                <Breadcrumb>
                    <BreadcrumbItem href="/">Index</BreadcrumbItem>
                    <BreadcrumbItem href="/workspace">Workspace</BreadcrumbItem>
                </Breadcrumb>
            </div>
            <div class="layout-content">
                <div class="layout-content-main">
                    <Row>
                        <div class="echarts">
                            <IEcharts :option="graph"></IEcharts>
                        </div>
                    </Row>
                </div>
            </div>
            <div class="layout-copy">
                2011-2017 &copy; AzureRM MAP
            </div>
            </Col>
        </Row>
    </div>
</template>
<script>
import IEcharts from "vue-echarts-v3/src/full.vue";
export default {
  name: "view",
  components: {
    IEcharts
  },
  data: () => ({
    spanLeft: 4,
    spanRight: 20,
    menuTheme: "dark",
    menuItems: [],
    graph: {
      title: {
        text: "Graph 简单示例"
      },
      tooltip: {},
      animationDurationUpdate: 1500,
      animationEasingUpdate: "quinticInOut",
      series: [
        {
          type: "graph",
          layout: "none",
          symbolSize: 50,
          roam: true,
          label: {
            normal: {
              show: true
            }
          },
          edgeSymbol: ["circle", "arrow"],
          edgeSymbolSize: [4, 10],
          edgeLabel: {
            normal: {
              textStyle: {
                fontSize: 20
              }
            }
          },
          data: [
            {
              name: "节点1",
              x: 300,
              y: 300
            },
            {
              name: "节点2",
              x: 800,
              y: 300
            },
            {
              name: "节点3",
              x: 550,
              y: 100
            },
            {
              name: "节点4",
              x: 550,
              y: 500
            }
          ],
          // links: [],
          links: [
            {
              source: 0,
              target: 1,
              symbolSize: [5, 20],
              label: {
                normal: {
                  show: true
                }
              },
              lineStyle: {
                normal: {
                  width: 5,
                  curveness: 0.2
                }
              }
            },
            {
              source: "节点2",
              target: "节点1",
              label: {
                normal: {
                  show: true
                }
              },
              lineStyle: {
                normal: { curveness: 0.2 }
              }
            },
            {
              source: "节点1",
              target: "节点3"
            },
            {
              source: "节点2",
              target: "节点3"
            },
            {
              source: "节点2",
              target: "节点4"
            },
            {
              source: "节点1",
              target: "节点4"
            }
          ],
          lineStyle: {
            normal: {
              opacity: 0.9,
              width: 2,
              curveness: 0
            }
          }
        }
      ]
    }
  }),
  computed: {
    iconSize() {
      return this.spanLeft === 4 ? 20 : 24;
    }
  },
  mounted: function() {},
  methods: {
    toggleClick() {
      if (this.spanLeft === 4) {
        this.spanLeft = 2;
        this.spanRight = 22;
      } else {
        this.spanLeft = 4;
        this.spanRight = 20;
      }
    }
  }
};
</script>

<style scoped>
.echarts {
  width: auto;
  height: 600px;
}
</style>
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
    box-shadow: 0 1px 1px rgba(0, 0, 0, .1);
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
    transition: width .2s ease-in-out;
}
</style>
<template>
    <div class="layout" :class="{'layout-hide-text': spanLeft < 5}">
        <Row type="flex">
            <Col :span="spanLeft" class="layout-menu-left">
            <div class="layout-logo">AzureRM MAP</div>
            <Menu :theme="menuTheme" width="auto">
                <Submenu name="1">
                    <template slot="title">
                        <Icon type="ios-paper"></Icon>
                        内容管理
                    </template>
                    <MenuItem name="1-1">文章管理</MenuItem>
                    <MenuItem name="1-2">评论管理</MenuItem>
                    <MenuItem name="1-3">举报管理</MenuItem>
                </Submenu>
            </Menu>
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
export default {
    data() {
        return {
            spanLeft: 4,
            spanRight: 20,
            menuTheme: 'dark'
        }
    },
    computed: {
        iconSize() {
            return this.spanLeft === 4 ? 20 : 24;
        }
    },
    mounted: function() {

    },
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
}
</script>
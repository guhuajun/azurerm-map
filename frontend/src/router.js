const routers = [{
    path: '/',
    meta: {
        title: ''
    },
    component: (resolve) => require(['./views/index.vue'], resolve)
}, {
    path: '/workspace',
    meta: {
        title: ''
    },
    component: (resolve) => require(['./views/workspace.vue'], resolve)
}];
export default routers;
const routes = [
   {
    path: '/',
    redirect: '/images' // 当访问根路径时，自动跳转到/images
  },
  {
    path: '/images',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '', component: () => import('pages/Images.vue')},
    ]
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes

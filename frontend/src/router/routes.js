const routes = [

  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path:'image',
        name:'ImagesPage',
        component: () => import('pages/ImagesPage.vue'),
      },
      {
        path:'update',
        name:'UpdatePage',
        component: () => import('pages/UpdatePage.vue'),
      },
    ],
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes

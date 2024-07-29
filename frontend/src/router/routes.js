const routes = [

  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        redirect: '/gallery'
       },
      {
        path:'gallery',
        name:'GalleryPage',
        component: () => import('pages/Gallery.vue'),
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

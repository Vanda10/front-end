const app = Vue.createApp({
    // template: '<h2>I am the template</h2>'
    data() {
        return{
            title: 'The final Empire',
            author: 'Brandon',
            age: 45
        }
    },
    methods: {
        changeTitle(title) {
            // console.log('You clicked me')
            this.title = title
        }

    }
  });
  
  app.mount("#app");
  
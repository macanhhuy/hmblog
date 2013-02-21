
$(function() {
    // Helper function to get a URL from a Model or Collection as a property
    // or as a function.


    //Todo model
    var Todo = Backbone.Model.extend({});


    var TodoList = Backbone.Collection.extend({
        model: Todo,

        // tastypie uri
        url: "/todo/todo/",
        getNextOrder: function(){
            if(!this.length){
                return 1;
            } else {
                return this.last().get("order") + 1;
            }
        }
    });

    var todoList = new TodoList;

    var TodoView = Backbone.View.extend({
        tagName: "li",
		
        template: _.template($("#item-template").html()),

        initialize: function() {

            _.bindAll(this, "clear","remove", "createOnEnter", "render");
            this.model.bind("destroy", this.remove);

        },

        render: function(){
            $(this.el).html(this.template(this.model.toJSON()));
            // convenient way for other function to get this element
          
            return this;
        }, 
        
        events: {
            
            "click .todo-destroy a": "clear",
            "click .check": "createOnEnter"
      
        },
        
        createOnEnter: function(event){
        	

        },
        clear: function() {

          this.model.destroy();
         

        }

    });


    var AppView = Backbone.View.extend({

        el: $("#todo-list"),

		
        
        initialize: function(){
            _.bindAll(this, "createOn", "addOne", "render");
            todoList.bind('reset', this.render);
            todoList.bind('add', this.addOne);
			todoList.fetch();
        },

        render: function() {
        	todoList.each(function(todo){
             $(this.el).append(new TodoView({model: todo}).render().el);
            },this);
            //return this;
            
            
             },
             events: {
            "keypress #create-todo-input": "createOn"
      
        },
        // add to view
        addOne: function(todo) {
            var todoView = new TodoView({model: todo});
             $(this.el).append(todoView.render().el);
        },
        createOn: function(event){
        	 if(event.keyCode != 13 || !$("#create-todo-input").val()) return;
            todoList.create({
                content: $("#create-todo-input").val(),
                done: false,
                order: todoList.getNextOrder()
            });
            $("#create-todo-input").val("");

        }
              
       
        
    });

    // start this app
    var appView = new AppView();

});



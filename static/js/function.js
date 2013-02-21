// load the following using JQuery's document ready function
$(function() {

	// Post model
	var Post = Backbone.Model.extend({});


	// define the collection of post
	var PostCollection = Backbone.Collection.extend({
		model : Post,

		url : '/api/v1/post/'
	});
	// set up the view for a post
	var PostView = Backbone.View.extend({
		template: _.template($("#postRowTpl").html()),
		tagName: "li",
		initialize : function() {

			_.bindAll(this, "createOnEnter","remove", "render");
			 this.model.bind("destroy", this.remove);

		},

		render : function() {
			// template with ICanHaz.js (ich)
			$(this.el).html(this.template(this.model.toJSON()));
            // convenient way for other function to get this element
          
            return this;
		},
		events : {

			"click span.delete" : "createOnEnter"

		},

		createOnEnter : function(event) {
			 this.model.destroy();

		}
	});

	// main app
	var AppView = Backbone.View.extend({
		tagName : 'tbody',

		initialize : function() {
			// instantiate a post collection
			this.post = new PostCollection();
			this.post.bind('reset', this.render, this);
			this.post.fetch();

		},

		render : function() {
			console.log("RENDERING APP");
			// template with ICanHaz.js (ich)
			this.post.each(function(p) {

				$(this.el).append(new PostView({
					model : p
				}).render().el);
			}, this);

			return this;
		}
	});

	var app = new AppView();
	$('#app').append(app.render().el);
}); 
const promBundle = require("express-prom-bundle");

export default ({ init }) => {
	init("routes.before", ({ app }) => {
		console.log("TEST")
		app.use(promBundle({ 
			includeMethod: true, 
			includePath: true,
			promClient: {
				collectDefaultMetrics: {
				}
			  } 
		}));
	});
};
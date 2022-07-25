# Deploying directus with docker-compose

Run `docker-compose up` to start directus with postgres database.

`/prom-metrics` is an API extension that uses the `express-prom-bundle` package to expose a `/metrics` endpoint that is compatible with prometheus to crawl from.

## Creating directus extensions

Directus extensions can be loaded into docker image by mounting volumes `/extensions/`.

### Adapting from [directus docs](https://docs.directus.io/extensions/creating-extensions/)

Scaffold a directus extension by running `npm init directus-extensions`. Develop the extension by editing the index.js in `/src` folder.

### Building the extension

Run `npm run build` to build the extension. Move the `index.js` under the `/dist` folder created by the previous command into the root folder.

### Developing extensions

#### App extensions

* [Interfaces](https://docs.directus.io/extensions/interfaces/)
* [Displays](https://docs.directus.io/extensions/displays/)
* [Layouts](https://docs.directus.io/extensions/layouts/)
* [Modules](https://docs.directus.io/extensions/modules/)
* [Panels](https://docs.directus.io/extensions/panels/)

#### API Extensions

* [Hooks](https://docs.directus.io/extensions/hooks/)
* [Endpoints](https://docs.directus.io/extensions/endpoints/)

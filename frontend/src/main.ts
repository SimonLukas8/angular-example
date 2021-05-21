import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { environment } from './environments/environment';

if (environment.production) {
  enableProdMode();
}

platformBrowserDynamic().bootstrapModule(AppModule) //creates a browser platform allowing Angular to be displayed in the Browser
  // the methods bootstrapModule takes the root component and renders it in the Browser
  .catch(err => console.error(err));

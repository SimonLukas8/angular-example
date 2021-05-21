import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import { TodoListComponent } from './component/todo-list/todo-list.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSliderModule } from '@angular/material/slider';
import {DragDropModule} from '@angular/cdk/drag-drop';
import { TodoComponent } from './component/todo/todo.component'; //leave out .ts


@NgModule({  //Angular Modules are data structures that combine building-blocks like components
  declarations: [  //defines content of the modules
    AppComponent,
    TodoListComponent,
    TodoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatSliderModule,
    BrowserAnimationsModule,
    DragDropModule
  ],
  providers: [],  //place for services, which contain logic for several components
  bootstrap: [AppComponent]  //bootstrap references to components which will be launched first. Normally this is AppComponent
})
export class AppModule { }

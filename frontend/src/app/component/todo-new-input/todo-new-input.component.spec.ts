import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TodoNewInputComponent } from './todo-new-input.component';

describe('TodoNewInputComponent', () => {
  let component: TodoNewInputComponent;
  let fixture: ComponentFixture<TodoNewInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TodoNewInputComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TodoNewInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

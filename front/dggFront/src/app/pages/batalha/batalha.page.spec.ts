import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BatalhaPage } from './batalha.page';

describe('BatalhaPage', () => {
  let component: BatalhaPage;
  let fixture: ComponentFixture<BatalhaPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(BatalhaPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

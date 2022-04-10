import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './common-services/auth.guard';
import { LoginComponent } from './login/login.component';
import { RolesComponent } from './roles/roles.component';
import { UsersComponent } from './users/users.component';

const routes: Routes = [
  {
    path: '',
    component : LoginComponent ,
    pathMatch : 'full',
  },{
    path: 'roles',
    component : RolesComponent ,
    canActivate : [ AuthGuard, ]
  },{
    path: 'users',
    component : UsersComponent ,
    canActivate : [ AuthGuard, ]
  },{
    path: 'login',
    component : LoginComponent ,
  },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {

}

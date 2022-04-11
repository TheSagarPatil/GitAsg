import { Component, OnInit } from '@angular/core';
import { RolesService } from '../common-services/roles.service';
import { RoleModel } from '../login/login';

@Component({
  selector: 'app-roles',
  templateUrl: './roles.component.html',
  styleUrls: ['./roles.component.css']
})
export class RolesComponent implements OnInit {
  errorMessage : string = '';
  rolesData: any;
  roleModel = new RoleModel('');
  currentUserRoles : string[] = [];
  constructor(
    private rolesService : RolesService
  ) { }

  ngOnInit(): void {
    this.getRoles();
    const userData = JSON.parse( localStorage.getItem('userData') || '' )
    this.currentUserRoles = userData?.roles || [];
  }
  getRoles(){
    this.rolesService.showRoles().subscribe(
      data => {
        this.rolesData = data.data ;
        console.log( data );
      },
      err => {
        console.log(err)
      }
    )
  }

  saveClicked($event : any) : void{
    this.rolesService.addRole(this.roleModel).subscribe(
      (data : any) => {
        console.log(data);
        this.errorMessage = 'success';
        this.getRoles();
      },
      (err : any ) => {
        console.log(err);
        this.errorMessage = 'fail';
      }
    )
  }
  onSubmit(){

  }
}

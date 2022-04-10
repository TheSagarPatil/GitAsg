import { KeyValuePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { forkJoin, Observable } from 'rxjs';
import { RolesService } from '../common-services/roles.service';
import { UserService } from '../common-services/user.service';
import { IRoleData, IUsersData, UserModel } from '../login/login';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
  errorMessage : string ='';
  userModel = new UserModel('','');
  usersData : any;
  rolesData: any;
  userData : any; // localStorage data
  currentUserRoles : string[] = [];
  constructor(
    private userService : UserService,
    private rolesService : RolesService,
    ) { }

  ngOnInit(): void {
    this.showUsers();
    this.userData = JSON.parse( localStorage.getItem('userData') || '' )
    this.currentUserRoles = this.userData.roles;
  }

  showUsers() : void {
    forkJoin(
      this.userService.showUsers(),
      this.rolesService.showRoles()
    ).subscribe(
      ([
        userData,
        rolesData
      ])=> {
        this.usersData = this.modifyData ( userData?.data || [] ) ;
        this.rolesData = rolesData.data;
        console.log(userData)
        console.log(rolesData)
      },
      err => {
        console.log(err)

      },
    )
  }
  onSubmit() : void{

  }

  saveClicked($event : any) : void{
    this.userService.addUser(this.userModel).subscribe(
      (data : any) => {
        console.log(data);
        this.errorMessage = 'success';
      },
      (err : any ) => {
        console.log(err);
        this.errorMessage = 'fail';
      }
    )
  }
  onSelectChange(event : any){
    console.log(this.userModel.roles)
    console.log(event);
    console.log(event.target.value);
    const SelectedItems : Set<string> = new Set();
    Array.from( event.target.selectedOptions) ?.forEach(
      (item : any) => {
        if(item.innerHTML){
          SelectedItems.add(item.innerHTML);
          console.log(item.innerHTML);
        }
      }
    )
    this.userModel.roles = [...SelectedItems.values()];
  }
  modelChange(event : any){
    this.selectedItems= event;
    console.log(event)
  }
  selectedItems : any[] = [];
  modifyData (userData : any){
    const dataArr : IRoleData[] = [];
    Object.keys ( userData )?.forEach(key => {
      const roleArray = userData[ key ];
      const roles = [];
      roleArray.forEach((role : any )=> {
        roles.push( role['ROLE'] )
      });
      dataArr.push({
        PHONE_NUMBER : key,
        ROLE : roleArray
      });
    });
    return dataArr;
  }

}

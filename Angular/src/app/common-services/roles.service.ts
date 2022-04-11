
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { QueryModel, RoleModel } from '../login/login';
import { Observable } from 'rxjs';
import { apiUrl } from '../models/_config';
import { catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RolesService {
  showRoleUrl = `${apiUrl}/showroles`;
  addRoleUrl = `${apiUrl}/addroles`;
  constructor(
    private http : HttpClient
  ) { }
  errorHandler(error : HttpErrorResponse){
    return throwError(error);
  }
  showRoles(queryModel ? : QueryModel) : Observable<any>{
    return this.http.post<any>(this.showRoleUrl, queryModel)
      .pipe(catchError(this.errorHandler));
  }
  addRole(roleModel : RoleModel) : Observable<any> {
    return this.http.post<any>(this.addRoleUrl, roleModel)
    .pipe(catchError(this.errorHandler));
  }
}

export class LoginModel {
    constructor (
        public phone_number : string,
        public password : string,
    ){}
}
export class UserModel {
    constructor (
        public phone_number : string,
        public password : string,
        public roles? : string[],
    ){}
}


export class QueryModel {
    constructor (
        public phone_number : string,
    ){}
}
export interface IRoleData {
    PHONE_NUMBER? : string,
    ROLE? : string,
}
export interface IUsersData {
    PHONE_NUMBER : string,
    ROLES : IRoleData[]
}
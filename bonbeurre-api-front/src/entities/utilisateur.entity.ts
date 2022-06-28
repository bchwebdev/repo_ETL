import { Entity, PrimaryGeneratedColumn, Column } from "typeorm"

@Entity('utilisateur')
export class UtilisateurEntity{

    @PrimaryGeneratedColumn({name : 'id'})
    id : number

    @Column({name : 'nom',length : 50})
    nom : string
    
    @Column({name : 'prenom',length : 50})
    prenom : string

    @Column({name : 'login',length : 100})
    login : string

    @Column({name : 'password',length : 100})
    password : string

    @Column({name : 'profil',length : 50})
    profil : string

}
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm"

@Entity({name : "unite"})
export class UniteEntity {

@PrimaryGeneratedColumn({name :'id'})
id : number

@Column({name :'numero'})
numero : number
}



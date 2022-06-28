import { Entity, PrimaryGeneratedColumn, Column, OneToOne } from "typeorm"
import { UniteEntity } from './unite.entity';

@Entity('automate')
export class AutomateEntity {

    @PrimaryGeneratedColumn({name : 'id'})
    id : number

    @Column({name : 'reference_type', length : 50})
    reference : string

    @OneToOne(()=> UniteEntity, (unite) => unite.id)
    id_unite : UniteEntity
}


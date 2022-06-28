import { Entity, PrimaryGeneratedColumn, Column, OneToOne } from "typeorm"
import { AutomateEntity } from './automate.entity';

@Entity('donnee-mesuree')
export class DonneeMesureeEntity {

@PrimaryGeneratedColumn({name : 'id'})
id : number

@Column({name : 'valeur', type : 'double' })
valeur : number

@Column({name : 'unite_mesure', length : 50 })
unite_mesure : number

@Column({name : 'date_heure', type :'datetime' })
date_heure : Date

@OneToOne(() => AutomateEntity, (automate) => automate.id)
id_automate : AutomateEntity

}
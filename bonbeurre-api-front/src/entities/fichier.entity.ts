import { Entity, PrimaryGeneratedColumn, Column } from "typeorm"

@Entity('fichier')
export class fichierEntity {

    @PrimaryGeneratedColumn({name : 'id'})
    id : number

    @Column({name : 'nom', length : 50})
    nom : string

    @Column({name : 'poid', type : 'float'})
    poid : number

    @Column({name : 'date_heure_creation',type :'datetime'})
    date_heure_creation : Date

    @Column({name : 'date_heure_envoi', type :'datetime'})
    date_heure_envoi : Date
}
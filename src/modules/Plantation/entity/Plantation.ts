import { v4 as uuidv4 } from 'uuid';
import {Entity, PrimaryColumn, Column} from "typeorm";


@Entity('Plantations')
class Plantation {

    @PrimaryColumn()
    id : String ;

    @Column()
    namePlantation : String;

    constructor(namePlantation : String){

        this.namePlantation = namePlantation;

        if(!this.id) this.id = uuidv4()

    }





}



export {Plantation}
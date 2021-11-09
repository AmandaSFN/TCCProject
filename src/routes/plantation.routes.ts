import {Router} from 'express'
import { CreatePlantationController } from '../modules/Plantation/UseCases/CreatePlantation/CreatePlantationController';
import { GetPlantationController } from '../modules/Plantation/UseCases/GetPlantation/GetPlantationController';
import { GetSituationController } from '../modules/Plantation/UseCases/GetSituation/GetSituationController';
import { RegisterSituationController } from '../modules/Plantation/UseCases/RegisterSituation/RegisterSituationController';

const plantationRoute = Router();



plantationRoute.post('/plantation/create-platation', (req,res)=>{
    const controller = new CreatePlantationController();
    controller.handle(req, res);
})

plantationRoute.post('/platation/register-situation',  (req,res)=>{
    const controller = new RegisterSituationController();
    controller.handle(req, res);
})


plantationRoute.get('/platation/get-plantation',  (req,res)=>{
    const controller = new GetPlantationController();
    controller.handle(req, res);
})


plantationRoute.patch('/platation/toggle-typeIrrigation',  (req,res)=>{
    console.log('Tipo de irrigação')
})


plantationRoute.get('/platation/activate-irrigation',  (req,res)=>{
    console.log('PLANTA IRRIGADA')
})


export {plantationRoute}
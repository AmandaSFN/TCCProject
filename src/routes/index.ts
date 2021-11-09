import {Router} from 'express'
import { plantationRoute } from './plantation.routes';

const routes = Router();



routes.use(plantationRoute)


export default routes
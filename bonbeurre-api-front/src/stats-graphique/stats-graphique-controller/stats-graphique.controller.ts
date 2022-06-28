import { Controller, Get, Param } from '@nestjs/common';

@Controller('stats-graphique')
export class StatsGraphiqueController {

    @Get('test')
    textConnectionApi(){
      
        console.log('CONNEXION API')
    }
}



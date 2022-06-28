import { Module } from '@nestjs/common';
import { StatsGraphiqueController } from './stats-graphique-controller/stats-graphique.controller';

@Module({
  controllers: [StatsGraphiqueController]
})
export class StatsGraphiqueModule {}

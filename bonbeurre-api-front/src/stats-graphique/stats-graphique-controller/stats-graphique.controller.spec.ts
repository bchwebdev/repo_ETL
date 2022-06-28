import { Test, TestingModule } from '@nestjs/testing';
import { StatsGraphiqueController } from './stats-graphique.controller';

describe('StatsGraphiqueController', () => {
  let controller: StatsGraphiqueController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [StatsGraphiqueController],
    }).compile();

    controller = module.get<StatsGraphiqueController>(StatsGraphiqueController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});

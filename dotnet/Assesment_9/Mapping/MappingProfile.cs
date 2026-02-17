using AutoMapper;
using Assesment_9.Models;
using Assesment_9.DTOs;

namespace Assesment_9.Mapping
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            CreateMap<Student, StudentDTO>().ReverseMap();
        }
    }
}

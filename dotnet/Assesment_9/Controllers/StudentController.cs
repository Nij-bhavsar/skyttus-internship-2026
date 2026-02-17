using Microsoft.AspNetCore.Mvc;
using Assesment_9.Data;
using Assesment_9.Models;
using Assesment_9.DTOs;
using AutoMapper;

namespace Assesment_9.Controllers
{
    [ApiController]
    [Route("api/v1/[controller]")]
    public class StudentController : ControllerBase
    {
        private readonly StudentRepository _repo;
        private readonly IMapper _mapper;

        public StudentController(StudentRepository repo, IMapper mapper)
        {
            _repo = repo;
            _mapper = mapper;
        }

        // GET ALL
        [HttpGet]
        public IActionResult GetStudents()
        {
            var students = _repo.GetAll();
            return Ok(_mapper.Map<List<StudentDTO>>(students));
        }

        // GET BY ID ✅
        [HttpGet("{id}")]
        public IActionResult GetStudentById(int id)
        {
            var student = _repo.GetById(id);

            if (student == null)
                return NotFound($"Student with ID {id} not found");

            return Ok(_mapper.Map<StudentDTO>(student));
        }

        // POST
        [HttpPost]
        public IActionResult AddStudent(StudentDTO dto)
        {
            var student = _mapper.Map<Student>(dto);
            _repo.Add(student);
            return CreatedAtAction(nameof(GetStudentById), new { id = student.Id }, dto);
        }

        // PUT
        [HttpPut]
        public IActionResult UpdateStudent(StudentDTO dto)
        {
            var student = _mapper.Map<Student>(dto);
            _repo.Update(student);
            return Ok(dto);
        }

        // DELETE
        [HttpDelete("{id}")]
        public IActionResult DeleteStudent(int id)
        {
            _repo.Delete(id);
            return Ok();
        }
    }
}
